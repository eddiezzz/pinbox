<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Login extends CI_Controller{

    function __construct(){
        parent::__construct();
        $this->load->helper('url');
        $this->load->model('login_model');

        $this->load->helper(array('form', 'url'));
          
        $this->load->library('form_validation');
        $this->form_validation->set_rules('username', 'username', 'required');
        $this->form_validation->set_rules('password', 'password', 'required');
    }

    public function index($msg)
    {
        if (! isset($msg))
        {
            $msg = 'welcome to pinbox';
        }
        $this->load->view('login', array('msg'=>$msg));
    }

    public function process()
    {
        $result = $this->login_model->validate();
        if(! $result)
        {
            $msg = '<font color=red>Invalid username and/or password.</font><br />';
            $this->index($msg);
        }else
        {
            redirect(base_url().'index.php/home/index');
        }        
    }

    public function regist()
    {
        $msg = 'welcome to pinbox';
        $this->load->view('register', array('msg'=>$msg));
    }
    public function doRegist()
    {
        /*
        if ($this->form_validation->run() == FALSE)
        {
            $this->index('error info');
            return;
        }
        */
        $result = $this->login_model->register();
        if(! $result)
        {
            $msg = '<font color=red>Invalid username and/or password.</font><br />';
            $this->index($msg);
        }else
        {
            redirect(base_url().'index.php/home/index');
        }        
    }
}
?>

<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');

class Home extends CI_Controller
{
    public $observe_fields;
	function __construct()
	{
		parent::__construct();
        log_message('error', 'log');
		$this->load->model('blog_model');
		$this->load->model('observe_model');
        $this->load->helper('url');
        $this->observe_fields = array();
	}

    function index()
	{
        $loggined = $this->check_isvalidated();

        //$topUserInfoArgs = array('username'=>$this->session->userdata('username'), 'title'=>"pinbox");
        $this->load->view("head_info", array('title'=>'pinbox'));

        $this->load->view("nav_bar", array('username'=>$this->session->userdata('username')));

        $bannerArgs = array('banner_title'=>'pinbox hero unit', 'banner_content'=>'this is a hero unit content written by sonny', 'btn_name'=>'detail');
        $this->load->view("banner",$bannerArgs);


        $fieldList = array('百度', '淘宝', '搜索', '存储', 'mysql', 'DBA');
        $eachHotNum = 7;
        foreach ($fieldList as $field)
        {
            $itemList = $this->blog_model->getHotSite($eachHotNum, $field);
            $fieldArgs = array('column_title'=>$field, 'column_href'=>'#', 'column_btn_name'=>'more', 'item_list'=>$itemList);
            $this->load->view("pin", $fieldArgs);
        }

                
        $topnBlogs = 15;
        $hotBlogs = $this->blog_model->getHotBlog($topnBlogs, 'field');
        $hotBlogArgs = array('column_title'=>'热门博客', 'column_href'=>'#', 'column_btn_name'=>'more', 'item_list'=>$hotBlogs);
		$this->load->view("pin", $hotBlogArgs);

        $this->load->view("footer", array('footer_content'=>"all rights reserved by sonny, 2013"));
	}

    private function check_isvalidated()
    {
        if(! $this->session->userdata('validated'))
        {
            log_message('info', 'user not loggin, redirect to login page');
            redirect(base_url().'index.php/login/index/to_login', 'refresh');
        }
    }

    public function logout()
    {
        $this->session->sess_destroy();
        redirect(base_url().'index.php/login/index/logout_success');
    }

    public function observe()
    {
    }
}
?>

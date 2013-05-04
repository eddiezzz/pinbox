<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');
class Login_model extends CI_Model{
    function __construct()
    {
        parent::__construct();
        $this->table = 'users';
    }

    public function validate()
    {
        $username = $this->security->xss_clean($this->input->post('username'));
        $password = $this->security->xss_clean($this->input->post('password'));

        $this->db->where('username', $username);
        $this->db->where('password', $password);

        $query = $this->db->get('users');
        if($query->num_rows() == 1)
        {
            $row = $query->row();
            $data = array(
                    'userid' => $row->userid,
                    'username' => $row->username,
                    'validated' => true
                    );
            $this->session->set_userdata($data);
            log_message('info', 'user name:'.$username.' password:'.$password.' login validate success');
            return true;
        }
        log_message('error', 'user name:'.$username.' password:'.$password.' login validate failed');
        return false;
    }

    public function register()
    {
        $username = $this->security->xss_clean($this->input->post('username'));
        $password = $this->security->xss_clean($this->input->post('password'));

        $data = array('username'=>$username, 'password'=>$password);
        $query = $this->db->insert('users', $data);
        $data['validated'] = true;
        $this->session->set_userdata($data);
        log_message('info', 'username:'.$username.' password:'.$password.' regist');
        return true;
    }

}
?>

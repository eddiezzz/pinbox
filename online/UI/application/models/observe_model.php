<?php if ( ! defined('BASEPATH')) exit('No direct script access allowed');
class observe_model extends CI_Model{
    function __construct()
    {
        parent::__construct();
    }

    public function get()
    {
        $username = $this->security->xss_clean($this->input->post('username'));
        $this->db->where('username', $username);

        $query = $this->db->get('user_observe');
        if($query->num_rows() == 1)
        {
            $row = $query->row();
            $words = $row->observes_fields;
            log_message('info', 'user name:'.$username.' observe_fields:'.$words);
            return explode(',', $words, 30);
        }
        log_message('error', 'user name:'.$username.' get observe_fields failed');
        return array();
    }
    public function update($fields)
    {
        $username = $this->security->xss_clean($this->input->post('username'));
        $this->db->where('username', $username);

        $query = $this->db->update('user_observe', implode($fields));
        log_message('info', 'user name:'.$username.' change observe_fields:'.$fields);
        return array();
    }

}
?>

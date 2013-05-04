<?php
class blog_model extends CI_Model
{
	function __construct()
	{
		parent::__construct();
        $this->load->database();
	}

	function getHotBlog($topn, $field)
	{
        $this->db->limit($topn);
        //$this->db->order_by('weight asc');
        //$query = $this->db->get('table_site_weight');
        $query = $this->db->get('table_site_link');
        $data = array();
        $i = 0;
        foreach ($query->result() as $row)
        {
            $item = array('name'=>$row->name, 'url'=>$row->link);
            $data[$i++] = $item;
        }
		return $data;
	}

    function getHotSite($topn, $field)
	{
        //select l.name, l.link from table_site_link as l, table_site_weight as w where l.link = w.link order by w.weight desc limit 10;

        $this->db->select('table_site_link.name, table_site_link.link');
        if (count($field))
        {
            $this->db->like('table_site_link.name', "$field");
        }
        $this->db->from('table_site_link');
        $this->db->join('table_site_weight', 'table_site_weight.link = table_site_link.link');
        $this->db->order_by('table_site_weight.weight desc');
        $this->db->limit($topn);
        $query = $this->db->get();
        $data = array();
        $i = 0;
        foreach ($query->result() as $row)
        {
            $item = array('name'=>$row->name, 'url'=>$row->link);
            $data[$i++] = $item;
        }
		return $data;
	}

}
?>

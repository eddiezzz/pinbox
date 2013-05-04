<div class="span4">
    <p><h3><?=$column_title?><a class="btn-small" href="<?=$column_href?>"><?=$column_btn_name?></a></h3></p>
    <ul>
    <?php foreach($item_list as $item):?>
        <li><a href="<?=$item['url']?>"><?=$item['name']?></a></li>
    <?php endforeach;?>
    </ul>
</div>


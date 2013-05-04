<td>
<div class='hotBlogDiv'>
<script type="text/javascript"></script>
    <font class='categoryTitle'>top<?=count($ItemList)?>博文</font>
    <a href='http://www.baidu.com'><font class='moreInfoButton'>[more</font></a><font id='closeHotBlog' class='moreInfoButton'>|close]</font>
    <ul>
    <?php foreach($ItemList as $item):?>
        <li><a href="<?=$item['url']?>"><?=$item['name']?></a></li>
    <?php endforeach;?>
    </ul>
</div>
</td>

<td>
<div class='hotSiteDiv'>
    <div width='100%' height='20px' border-style='solid' border-color='red'>
    <font class='categoryTitle'>主题推荐站点</font>
    <a href='http://www.baidu.com'><font class='moreInfoButton'>[more</font></a><font id='closeHotSite' class='moreInfoButton'>|close]</font>
    </div>
    <?php foreach($fieldList as $field):?>
        <ul>
        <h3><?=$field['fieldName']?></h3>
        <?php foreach($field['itemList'] as $item):?>
            <li><a href="<?=$item['url']?>"><font class='listItemFont'><?=$item['name']?></font></a></li>
        <?php endforeach;?>
        </ul>
    <?php endforeach;?>
</div>
</td>

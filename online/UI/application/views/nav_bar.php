<div class="navbar navbar-inverse navbar-fixed-top">
  <div class="navbar-inner">
    <div class="container">
      <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="brand" href="#">Pinbox</a>
      <div class="nav-collapse collapse">
        <ul class="nav nav-pills">
          <li class="active"><a href="#">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
            <ul class="dropdown-menu">
              <li><a href="#">Action</a></li>
              <li><a href="#">Another action</a></li>
              <li><a href="#">Something else here</a></li>
              <li class="divider"></li>
              <li class="nav-header">Nav header</li>
              <li><a href="#">Separated link</a></li>
              <li><a href="#">One more separated link</a></li>
            </ul>
          </li>
        </ul>
        <form class="navbar-search pull-left" action="">
            <input type="text" class="search-query span2" placeholder="Search">
        </form>
        <ul class="nav pull-right">
        <li><a href='www.baidu.com'><?=$username?></a></li>
        <li><a href=<?=base_url()?>index.php/home/observe>领域订阅</a></li>
        <li><a href=<?=base_url()?>index.php/home/logout>logout</a></li>
        </ul>
        <!--form class="navbar-form pull-right">
          <input class="span2" type="text" placeholder="Email">
          <input class="span2" type="password" placeholder="Password">
          <button type="submit" class="btn">Sign in</button>
        </form-->
      </div><!--/.nav-collapse -->
    </div>
  </div>
</div>



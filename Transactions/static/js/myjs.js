$(document).ready(function(){
  
    // alert("We are all set!");
    
    $('.table').paging({ limit:15, }); 


      // Scroll Top Script
   //Check to see if the window is top if not then display button
   $(window).scroll(function(){
    if ($(this).scrollTop() > 10) {
      $('.scrollToTop').fadeIn();
    } else {
      $('.scrollToTop').fadeOut();
    }
  });

  //Click event to scroll to top
  $('.scrollToTop').click(function(){
    $('html, body').animate({scrollTop : 0},100);
    return false;
  });
 //END Scroll Top Script
   
  });
var idList=[];
var posterList=[];
function processQuery(obj) {
  var http=new XMLHttpRequest();
  http.async=true;
  var imdbTitle = document.getElementById('searchtxt').value;

  http.open("GET", "http://www.omdbapi.com/?s=" + imdbTitle, false);
  http.send(null);
  // Response to JSON
  var omdbData = http.responseText;
  var omdbJSON = eval("(" + omdbData + ")");
  if(omdbJSON.Response == 'False'){
    // alert('oops there is error');
    $('#suggestions-failure').css('display','block');
    $('#suggestions-success').css('display','none');
    $('#thumbnail-grid').css('display','none');
  }else{
    $('#suggestions-failure').css('display','none');
    $('#suggestions-success').css('display','block');
    $('#thumbnail-grid').css('display','block');
  }
  idList=[];
  // alert(omdbJSON.Search.length);
  $(omdbJSON.Search).each(function(index){
    idList[index]=omdbJSON.Search[index].imdbID;
  });

  $(idList).each(function(index){
    if(index<=4){
    http.open("GET", "http://www.omdbapi.com/?i=" + idList[index], false);
    http.send(null);
    omdbData = http.responseText;
    omdbJSON = eval("(" + omdbData + ")");
    var imgStr='#img'+index;
    var alttxt='Title: '+omdbJSON.Title+'\tYear:'+omdbJSON.Year+
                                            '\tRating:'+omdbJSON.imdbRating;
    $(imgStr).attr('alt',alttxt);
    // alert(omdbJSON.Poster);

    if(omdbJSON.Poster != 'N/A'){
      var image = new Image();
      image.src = omdbJSON.Poster;
      image.onload = function(){
        //image.src = omdbJSON.Poster;
        $(imgStr).attr('src',$(this).attr('src'));
      }

      // $(imgStr).attr('src',image.src);

    }else{
      // $(imgStr).attr('style','height:30px');
      // $(imgStr).attr('style','width:50px');
      // $(imgStr).attr('src','/someDummy/picture.png');
    }
    }
  });
  return idList;
}

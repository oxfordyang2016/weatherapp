$(function(){

	
	myAjax();
	

});	

function myAjax(params)
{

	$.ajax({
		cache:false,
		method ："POST",
		async : true,
		url :"https://yangmingweatherapp.herokuapp.com/python/",
		data :params,
		datatype : "json",
		beforeSend : function(){
          
		} ,
		success : function(result){
			console.log(result);
		},
		error ：function(XMLHttpRequest, textStatus, errorThrown){

		},
		complete: function(){

		}

	});

}


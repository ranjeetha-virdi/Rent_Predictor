function getBathroomsValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
function getBedroomsValue() {
    var uiBHK = document.getElementsByName("uiBedrooms");
    for(var i in uiBedrooms) {
      if(uiBedrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

function onClickedEstimateRent() {
    console.log("Estimated Rent button clicked");

    var state = document.getElementById("uiState");
    var category = document.getElementById("uiCategory");
    var bathrooms = getBathroomsValue();
    var bedrooms = getBedroomsValue();
    var fee = document.getElementById("uiFee");
    var pets_allowed = document.getElementById("uiPets");
    var square_feet = document.getElementById("uiSqft");
    var cityname = document.getElementById("uiCity");
    var with_storage = document.getElementById("uiStorage");
    var with_parking = document.getElementById("uiParking");
    var with_gym = document.getElementById("uiGym");
    var with_pool = document.getElementById("uiPool");
    var with_woodfloors = document.getElementById("uiWood_floors");
    var with_patio = documnet.getElementById("uiPatio");
    var with_clubhouse = document.getElementById("uiClubhouse");
    var with_internet = document.getElementById("uiInternet");
    var with_gated = document.getElementById("uiGated");
    var est_rent = document.getElementById("uiEstimatedRent")


var url = "http://127.0.0.1:5000/Predict"; //URL of the Flask Server
    // $.post is a jquery post call 
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/Predict" , data:JSON.stringify({
        state: state.value,
        category: category.value,
        bathrooms: bathrooms,
        bedrooms: bedrooms,
        fee: fee.value,
        pets_allowed : pets_allowed.value,
        square_feet: parseFloat(square_feet.value),
        cityname: cityname.value,
        with_storage : with_storage.value,
        with_parking : with_parking.value,
        with_gym : with_gym.value,
        with_pool : with_pool.value,
        with_woodfloors : with_woodfloors.value,
        with_patio : with_patio.value,
        with_clubhouse : with_clubhouse.value,
        with_internet : with_internet.value,
        with_gated : with_gated.value
    }),contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function(data, status) {
        console.log(data.estimated_rent);
        est_rent.innerHTML = "<h2>" + data.estimated_rent.toString() + " $</h2>";
        console.log(status);
    }
    });
}

//function onPageLoad() {
 // console.log( "document loaded" );
 // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  
//}


  window.onload = onClickedEstimateRent;
/*jshint esversion: 6 */

function calc() {
    var total = document.getElementById("player").innerHTML;
    for (let i = 0; i<=total; i++) {
    var num1 = document.getElementsByClassName("attended_sessions")[i].innerHTML;
    var num2 = document.getElementsByClassName("total_sessions")[i].innerHTML;
    var num3 = (parseInt(num1)*100) / parseInt(num2);
    document.getElementsByClassName("result")[i].innerHTML = num3.toFixed(0);
    }  
}


function traffic_light() {
    var total = document.getElementById("player").innerHTML;
    for (let i = 0; i <=total; i++) {
        var num1 = document.getElementsByClassName("result")[i].innerHTML;
        if (num1 <=10 ){ 
            document.getElementsByClassName("traffic_light")[i].style.backgroundColor ='#FF0000';} 
        else if (num1 >=11 && num1 <= 50){
            document.getElementsByClassName("traffic_light")[i].style.backgroundColor ='#FFA500';}
        else if (num1 >= 51 && num1 <=80){
            document.getElementsByClassName("traffic_light")[i].style.backgroundColor ='#FFFF22';}
        else {
            document.getElementsByClassName("traffic_light")[i].style.backgroundColor ='#26A916';  
        }
   
    }
}


function game_name(){
    var forms = document.querySelector("#id_team_selection_set-TOTAL_FORMS").value;
    for (let i = 0; i <= forms; i++){
    var target = document.getElementsByClassName("form-select selectmultiple form-control")[i];
    var text = target.options[target.selectedIndex].text;
    document.getElementsByClassName("player_name")[i].innerHTML = text;
    } 
}





    
  
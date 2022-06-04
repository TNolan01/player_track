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
        num1 = document.getElementsByClassName("result")[i].innerHTML;
        if (num1 = 'NaN'){ 
            document.getElementsByClassName('traffic_light')[i].style.backgroundColor ='#EA160C';} 
        else if (num1 <= 40){
            document.getElementsByClassName('traffic_light')[i].style.backgroundColor ='#EA160C';}
        else if (num1 > 40 && num1 <=70){
            document.getElementsByClassName('traffic_light')[i].style.backgroundColor ='#EA850C'}
        else {
            document.getElementsByClassName('traffic_light')[i].style.backgroundColor ='#26A916';   
        }
    console.log(num1);
    }
}
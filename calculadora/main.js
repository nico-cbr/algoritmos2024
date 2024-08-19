let num1;
let num2;
let total;

//armazena os valores do input
function entrada(){
  num1 = Number(document.getElementById("n1").value);
  num2 = Number(document.getElementById("n2").value);

    // num1 = parseFloat(num1);
  // num2 = parseFloat(num2);
}

function somar(){
  entrada()
  total = document.getElementById("resultado");
  total.innerHTML = num1 + num2;  
}

function subtrair(){
  entrada()
  total = document.getElementById("resultado");
  total.innerHTML = num1 - num2;  
}

function dividir(){
  entrada()
  total = document.getElementById("resultado");
  total.innerHTML = num1 / num2;  
}

function multiplicar(){
  entrada()
  total = document.getElementById("resultado");
  total.innerHTML = num1 * num2;  
}

function apagar(){
  total = document.getElementById("resultado");
  total.innerHTML = "";
  document.getElementById("n1").value="";
  document.getElementById("n2").value="";
}

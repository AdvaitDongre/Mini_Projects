function openPopup(userType) {
    document.getElementById("loginPopup").style.display = "block";
    document.getElementById("loginPopup").style.justifyContent = "center";
    document.getElementById("userType").textContent = userType;
}
function openPopupADMIN(){
    document.getElementById("loginPopup-ADMIN").style.display ="block";
    document.getElementById("loginPopup").style.justifyContent = "center";
}
function openPopupEMP(){
    document.getElementById("loginPopup-EMPLOYEE").style.display="block";
    document.getElementById("loginPopup").style.justifyContent = "center";
}
function closePopup() {
    document.getElementById("loginPopup-ADMIN").style.display = "none";
    document.getElementById("loginPopup-EMPLOYEE").style.display = "none";
}

function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "admin" && password === "admin123") {
        alert("Admin login successful!");
        closePopup();
    }
}

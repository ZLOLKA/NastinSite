function showHide(thisObj, obj)
{
    console.log(obj.style.left);
    var startPosition = (obj.style.left).toString().slice(0, -2);

    if (obj.style.left == "-390px")
    {
        alert(obj);
        thisObj.style.transform = 'rotate(180deg)'
    }
    else
    {
        //document.getElementsByClassName('Menu')[0].style.left = '-390px';
        thisObj.style.transform = 'rotate(0deg)'
    }
}
function aOver(obj) {
    obj.style.textDecoration = 'underline';
}
function aOut(obj) {
    obj.style.textDecoration = 'none';
}

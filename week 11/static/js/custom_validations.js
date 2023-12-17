
function validate(event){
    v = document.getElementById("email").value;

    if(v.indexOf("@") == -1){
        event.preventDefault();
        alert("Enter a valid email");
        return false;
    }
    return true;
}

function thanks(article, response){
    var div = document.createElement('div');
    div.class = 'message';
    div.innerHTML = "Thank you for liking";
    article.parentNode.appendChild(div);
}

function send_like(event){
    article = event.target
    article_id = article.dataset.article_id

   

    fetch("/article_like/" + article_id).then(
        response=>thanks(article, response)
    ).catch(
        err=>console.log(err)
    )
}

function init(){
    like_buttons = document.querySelectorAll(".like-button");
    for(const like_button of like_buttons){
        like_button.onclick = send_like;
    }
}
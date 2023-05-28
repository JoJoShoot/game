var queryForm = document.getElementById("queryForm");
var queryBtn = document.getElementById("queryBtn");
var downloadBtn = document.getElementById("downloadBtn");
var resultDiv = document.getElementById("result");

var selectedTags = [];

queryForm.addEventListener("submit", function (event) {
event.preventDefault();
var tagsInput = document.getElementById("tagsInput");
selectedTags = tagsInput.value.split(",");

var xhr = new XMLHttpRequest();
xhr.open("GET", "/query?tags=" + selectedTags.join(","));

xhr.onload = function () {
if (xhr.status == 200) {
resultDiv.innerHTML = "共有 " + xhr.responseText + " 条数据。";
downloadBtn.disabled = false;
} else {
console.error("Error:", xhr.statusText);
}
};

xhr.send();
});

function downloadFile(url) {
	// 创建一个隐藏的a标签
	var link = document.createElement("a");
	link.style.display = "none";
	link.href = url;

  xhr.onload = function () {
    if (xhr.status == 200) {
      downloadFile(xhr.responseText);
      showSuccessMessage("文件下载成功！");
    } else {
      console.error("Error:", xhr.statusText);
    }
  };



// 添加download属性
link.download = url.split("/").pop();

// 将a标签添加到页面中，并模拟点击
document.body.appendChild(link);
link.click();

// 删除a标签
document.body.removeChild(link);
}

downloadBtn.addEventListener("click", function () {
var xhr = new XMLHttpRequest();
xhr.open("GET", "/download?tags=" + selectedTags.join(","));

xhr.onload = function () {
if (xhr.status == 200) {
downloadFile(xhr.responseText);
} else {
console.error("Error:", xhr.statusText);
}
};

xhr.send();
});
async function increase() {
    let res = await fetch("http://127.0.0.1:5000/increase");
    let data = await res.json();
    document.getElementById("count").innerText = data.count;
}

async function decrease() {
    let res = await fetch("http://127.0.0.1:5000/decrease");
    let data = await res.json();
    document.getElementById("count").innerText = data.count;
}
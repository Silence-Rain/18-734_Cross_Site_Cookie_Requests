var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://silence-rain.cn:9888?actual=1&type=send', true);
xhr.send("test");

try {
    var myRequest = new Request('http://silence-rain.cn:9888?actual=1&type=fetch');
    fetch(myRequest);
} catch (e) {
    console.log('fetch: ', e);
}
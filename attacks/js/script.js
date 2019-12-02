var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://silence-rain.cn:9888?ad_type=1&type=send', true);
xhr.withCredentials = true;
xhr.send();

try {
    var myRequest = new Request('http://silence-rain.cn:9888?ad_type=1&type=fetch', {credentials: 'include'});
    fetch(myRequest);
} catch (e) {
    console.log('fetch: ', e);
}
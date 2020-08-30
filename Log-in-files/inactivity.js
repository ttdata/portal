function idleLogOut() {
    var time = resetTimer;
    var time2 = resetTimer;
    window.onmousemove = resetTimer;
    window.onmousedown = resetTimer;
    window.onclick = resetTimer;
    window.onscroll = resetTimer;
    window.onkeypress = resetTimer;

    async function logout() {
        const res = await fetch('http://ttdata.life:7961/auth/logout', {
            method: 'POST',
            credentials: 'include',
        })
        const body = await res.json()
        if (body.status === 'error') {
            alert(body.message)
            return
        }
        user = null
        render()
    }

    function warning() {
        window.alert("You will be logged out for inactivity soon");
    }

    function resetTimer() {
        clearTimeout(time);
        clearTimeout(time2)
        time = setTimeout(logout, 900000);
        time2 = setTimeout(warning, 840000)
    }
}

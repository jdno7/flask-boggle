const $guessForm = $('form')
const $timer = $('#timer').text(`Time Remaining 1:00`)
const $gamesPlayed = $('#games-played')
const $bestScore = $('#best-score')
let gameLength = 60
let score = 0
setTimeout(async function(){
    
    const response = await axios.post('/game-over', {"score": score})
    $gamesPlayed.text(`Games Played: ${response.data.games_played}`)
    $bestScore.text(`Best Score: ${response.data.best_score}`)
    const new_board = response.data.new_board

    alert('Time is UP! Start New Game')

    window.location.reload()


},60000)

function countDown(){
    gameLength -- 
    if (gameLength < 10) {
    $('#timer').text(`Time Remaining 0:0${gameLength}`)
    }
    else{
    $('#timer').text(`Time Remaining 0:${gameLength}`)
    }
}

$('document').ready(setInterval(countDown, 1000))



async function submitBoggleGuess(evt){
    evt.preventDefault()
    $guess = $('input').val()
    // const response = await axios.get(`/check-word?user-guess=${$guess}`)
    const response = await axios.get('/check-word', {params: {'user-guess': $guess} })
    // alert(response.data.results)
    $('#user-guess').text(response.data.results)
    const res = response.data.results
    if ( res === "ok"){
        score += $guess.length
        $('#user-score').text(`Your Score: ${score}`)
    }

}

$guessForm.on('submit', submitBoggleGuess)
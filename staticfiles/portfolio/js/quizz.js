
const quizData = [
    {
        question: "Que linguagem é usada no browser para back-end?",
        a: "Java",
        b: "C",
        c: "Python",
        d: "Javascript",
        correct: "d",
    },
    {
        question: "O que quer dizer CSS?",
        a: "Central Style Sheets",
        b: "Cascading Style Sheets",
        c: "Cascading Simple Sheets",
        d: "Central Simple Sheets",
        correct: "b",
    },
    {
        question: "O que quer dizer HTML?",
        a: "Hypertext Markup Language",
        b: "Hypertext Markdown Language",
        c: "Hyperloop Machine Language",
        d: "Hyperloop Markup Language",
        correct: "a",
    },
    {
        question: "Qual destas opções é o framework usado pelo Spotify",
        a: "Ruby on Rails",
        b: "Django",
        c: "jQuery",
        d: "React",
        correct: "b",
    },
    {
        question: "Qual destas opções é o framework usado pelo Spotify",
        a: "Ruby on Rails",
        b: "Django",
        c: "jQuery",
        d: "React",
        correct: "b",
    },


];

const nome = document.getElementById('nome')
const quiz= document.getElementById('quiz')
const answerEls = document.querySelectorAll('.answer')
const questionEl = document.getElementById('question')
const a_text = document.getElementById('a_text')
const b_text = document.getElementById('b_text')
const c_text = document.getElementById('c_text')
const d_text = document.getElementById('d_text')
const submitBtn = document.getElementById('submit')


let currentQuiz = 0
let score = 0

loadQuiz()

function loadQuiz() {

    deselectAnswers()

    const currentQuizData = quizData[currentQuiz]

    questionEl.innerText = currentQuizData.question
    a_text.innerText = currentQuizData.a
    b_text.innerText = currentQuizData.b
    c_text.innerText = currentQuizData.c
    d_text.innerText = currentQuizData.d
}

function deselectAnswers() {
    answerEls.forEach(answerEl => answerEl.checked = false)
}

function getSelected() {
    let answer
    answerEls.forEach(answerEl => {
        if(answerEl.checked) {
            answer = answerEl.id
        }
    })
    return answer
}


submitBtn.addEventListener('click', () => {
    const answer = getSelected()
    if(answer) {
       if(answer === quizData[currentQuiz].correct) {
           score++
       }

       currentQuiz++

       if(currentQuiz < quizData.length) {
           loadQuiz()
       } else {
           quiz.innerHTML = `
           <h2>Acertaste ${score}/${quizData.length} questões de forma correta</h2>

           <button onclick="location.reload()">Reload</button>
           `
       }
      var objecto = new PontuacaoQuizz();
      objecto.nome = nome
      objecto.score = score
      objecto.save()
    }
})
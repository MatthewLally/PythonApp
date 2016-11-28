// adapted from http://codepen.io/jezebelee/pen/dpJVwq 
//sets up an array of quotes
var quotes = ['Imagination is more important than knowledge. - Albert Einstein', 
  'If music be the food of love, play on. - William Shakespheare',
  'The way to get started is to quit talking and begin doing. - Walt Disney',
  'Obstacles are those frightful things you see when you take your eyes off the goal. - Henry Ford',
  'I skate where the puck is going to be, not where it has been. - Wayne Gretzky',
  'When you come to a fork in the road, take it. - Yogi Berra',
  'We may affirm absolutely that nothing great in the world has been accomplished without passion. - Hegel',
  'The life which is unexamined is not worth living. - Socrates',
  'Live as if you were to die tomorrow. Learn as if you were to live forever. - M.K. Gandhi',
  'What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar',]
function newQuote() { //creates a function new quote
var randomNumber = Math.floor(Math.random() * (quotes.length)); // creates a random number buy multiplying a random number by quotes.length
document.getElementById('quoteDisplay').innerHTML = quotes[randomNumber]; //prints out random quote
}
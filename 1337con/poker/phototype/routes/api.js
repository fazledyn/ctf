const express = require('express')
const unflatten = require('unflatten')
const pug = require('pug');
const router = express.Router()


function getRandomInt(max) {
	return Math.floor(Math.random() * max * max * max);
  }

router.post('/submit', (req, res) => {
    const { song } = unflatten(req.body);
	var randoms = getRandomInt(10);
	let finalname = "Guest"+randoms;
	if (song.name.includes('King') || song.name.includes('AST Ace Of Spades	') || song.name.includes('Diamonds') || song.name.includes('polluting Poker')) {
		return res.json({
			'response': pug.compile('span Hello #{user}, thank you for letting us know!')({ user:finalname })
		});
	} else {
		return res.json({
			'response': 'Please provide us with the name of an existing Card.'
		});
	}
});

module.exports = router
const express = require('express');
var cors = require('cors')
const app = express();

app.set('view engine', 'pug');
app.use(express.static("public"))
app.use(express.json())
app.use(cors())

app.get('/', (req, res) => {
    res.render('index')
})


app.listen(3022, ()=> {console.log("server listing on http://127.0.0.1:3022")});


const userRouter = require('./routes/api');


app.use('/api', userRouter);
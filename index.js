import express from "express";
import bodyParser from "body-parser";
import spawn from "cross-spawn";

const app = express();
const port = 3000;
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.listen(port, () =>{
    console.log("Server running on port " + port);
});

app.get("/", (req, res) =>{
    res.render("index.ejs");
});

app.post("/getResponse", (req, res) =>{
    const query = req.body.userQuery;
    const process = spawn('python', ["./chatbot.py", query]);
    process.stdout.on('data', function(data){
        res.send(data.toString());
    });
});
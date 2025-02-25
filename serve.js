const express = require("express");
const cors = require("cors");
const axios = require("axios"); // 用于请求 FastAPI
const { exec } = require('child_process');
const app = express();
const PORT = 8082; // 本地代理端口
const server = app.listen(8085, () => console.log('Server running on port 8085'));
server.setTimeout(120 * 1000);

exec('python main.py', (error, stdout, stderr) => {
    if (error) {
        console.error(`执行 Python 脚本失败: ${error.message}`);
        return;
    }
    if (stderr) {
        console.error(`Python 脚本错误: ${stderr}`);
        return;
    }
    console.log(`Python 脚本输出: ${stdout}`);
});

setTimeout(() => {
console.log("Python 脚本执行完成");
},5000);
app.use(cors());
app.use(express.json());
const cache=new Map();

// 调用 FastAPI 获取 A 股数据
app.get("/stocks", async (req, res)=> {

    console.log("收到 /stocks 请求")
    try {
        const cachedData = cache.get("stocks");
        if (cachedData) {
            console.log("使用缓存数据");
            return res.json(cachedData);
        }
       const response = await axios.get("http://localhost:8085/stocks"); // 请求 FastAPI
       cache.set("stocks", response.data);
       res.json(response.data);
    } catch (error) {
        console.error("获取股票数据失败:", error);
        res.status(100).json({ error: "无法获取股票数据" });
    }
});

// 调用 FastAPI 获取加密货币数据
app.get("/crypto", async (req,res) => {
    console.log("收到 /crypto 请求");
    try {
        const cachedData = cache.get("crypto");
        if (cachedData) {
            console.log("使用缓存数据");
            return res.json(cachedData);
        }
        const response = await axios.get("http://localhost:8085/crypto"); // 请求 FastAPI
        cache.set("crypto", response.data);
        res.json(response.data);
    } catch (error) {
        console.error("获取加密货币数据失败:", error);
        res.status(100).json({ error: "无法获取加密货币数据" });
    }
});
// app.get("/options", async (req,res) => {

//     console.log("收到 /options 请求");
//     try {
//        const response = await axios.get("http://localhost:8085/options"); // 请求 FastAPI
//        res.json(response.data);
//     } catch (error) {
//         console.error("获取股票数据失败:", error);
//         res.status(100).json({ error: "无法获取股票数据" });
//     }
// });

// 启动 Express 服务器
app.listen(PORT, () => {
    console.log(`服务器启动成功，正在监听端口 ${PORT}`);
});

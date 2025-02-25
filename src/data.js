// const { exec } = require('child_process');

// function getRealTimeData(callback) {
//     exec('python data.py', (error, stdout, stderr) => {
//         if (error) {
//             console.error(`执行 Python 失败: ${error.message}`);
//             return callback(error, null);
//         }

//         if (stderr) {
//             console.error(`Python 执行错误: ${stderr}`);
//             return callback(new Error(stderr), null);
//         }

//         try {
//             if (!stdout) {
//                 return callback(new Error("Python 脚本返回空数据"), null);
//             }

//             const data = JSON.parse(stdout);
//             callback(null, data);
//         } catch (parseError) {
//             console.error(`JSON 解析失败: ${parseError.message}`);
//             callback(parseError, null);
//         }
//     });
// }

// module.exports = getRealTimeData;

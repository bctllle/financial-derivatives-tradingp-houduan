const mysql = require('mysql2/promise');

// 创建 MySQL 连接池
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: '123456',
  database: 'users',  // 你的数据库名
  connectionLimit: 10
});

const UserModel = {
  // 通过账号查找用户
  async findByAccount(account) {
    const [rows] = await pool.query('SELECT * FROM users WHERE account = ?', [account]);
    return rows.length > 0 ? rows[0] : null;
  },

  // 通过钱包地址查找用户
  async findByWalletAddress(walletAddress) {
    const [rows] = await pool.query('SELECT * FROM users WHERE wallet_address = ?', [walletAddress]);
    return rows.length > 0 ? rows[0] : null;
  },

  // 创建新用户（传统注册）
  async create(account, hashedPassword) {
    const userId = generateUUID();
    await pool.query('INSERT INTO users (id, account, password) VALUES (?, ?, ?)', [userId, account, hashedPassword]);
  },

  // 创建新用户（MetaMask 注册）
  async createWithWallet(walletAddress) {
    const userId = generateUUID();
    await pool.query('INSERT INTO users (id, wallet_address) VALUES (?, ?)', [userId, walletAddress]);
  },

  // 更新用户的钱包地址
  async updateWalletAddress(userId, walletAddress) {
    await pool.query('UPDATE users SET wallet_address = ? WHERE id = ?', [walletAddress, userId]);
  }
};

// 生成 UUID
function generateUUID() {
  // 你可以选择其他生成 UUID 的方法
  return require('uuid').v4();
}

module.exports = UserModel;

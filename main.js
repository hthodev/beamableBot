import fs from "fs/promises";
import { HttpsProxyAgent } from "https-proxy-agent";
import fetch from "node-fetch";
import chalk from "chalk";
import readline from 'readline/promises';


// Helper Function: Logger
function logger(message, level = "info") {
  const now = new Date().toISOString();
  const colors = {
    info: chalk.blue,
    warn: chalk.yellow,
    error: chalk.red,
    success: chalk.green,
    debug: chalk.magenta,
  };
  const color = colors[level] || chalk.white;
  console.log(color(`[${now}] [${level.toUpperCase()}]: ${message}`));
}

const headers = {
  "accept": "text/x-component",
  "accept-language": "en-US,en;q=0.9,vi;q=0.8",
  "content-type": "text/plain;charset=UTF-8",
  "next-router-state-tree": "%5B%22%22%2C%7B%22children%22%3A%5B%5B%22host%22%2C%22hub.beamable.network%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22modules%22%2C%7B%22children%22%3A%5B%5B%22moduleIdOrPath%22%2C%22questsold%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%5B%22moduleNestedId1%22%2C%227570%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fmodules%2Fquestsold%2F7570%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
  "priority": "u=1, i",
  "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"Windows\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "Referer": "https://hub.beamable.network/modules/questsold/7571",
  "Referrer-Policy": "strict-origin-when-cross-origin"
};

async function readFiles() {
  const proxyStr = await fs.readFile("proxies.txt", "utf-8");
  const proxies = proxyStr.trim().split("\n").map(proxy => proxy.trim());
  const cookieData = await fs.readFile("cookies.txt", "utf-8");
  const cookies = cookieData.trim().split("\n").map(cookie => cookie.trim());
  return { proxies, cookies };
}

async function clickQuest(cookie, agent, nonce) {
    try {
      const response = await fetch(`https://gist.githubusercontent.com/hthodev/d34feb751b2314dd8abdfa4f1b2b60a4/raw/beamable_quest.txt`, {
        method: "GET",
        agent
      });
      logger("Đang kiểm tra có quest nào vừa thêm mới không?")
  
      const res = await response.text();
      if (!res || res === 'none') {
        logger("Không có quest nào mới thêm vào")
        return;
      }

      const quests = res.trim().split('\n').map(quest => quest.trim());
      const questAsync = []
      for (const quest of quests) {
        const [questId, body] = quest.split('||').map(data => data.trim())
        const url = `https://hub.beamable.network/modules/questsold/${questId}`
        headers["next-action"] = "7f88f675202a5b494db75a56741697346cbe35156f"
        headers["cookie"] = cookie
        const bodyNonce = body.replace('uuid', nonce)
        questAsync.push(fetch(url, {
          method: 'POST',
          headers,
          agent,
          body: bodyNonce
        })) 
        
        logger(`Đang click quest ${questId}`,)
      }
      await Promise.all(questAsync)
      logger("Đã click tất cả các quest thêm mới.", "success")

  
    } catch (error) {
      logger(`Lỗi quest: ${error.message}`, 'error')

    }
}

async function completeQuest(cookie, agent) {
    try {
      const response = await fetch(`https://gist.githubusercontent.com/hthodev/ce040c0cb8cc5a3e0a01b47556237225/raw/beamable_complete_quest.txt`, {
        method: "GET",
      });
      const res = await response.text();
      if (!res || res === 'none') {
        return;
      }
  
      const quests = res.trim().split('\n').map(quest => quest.trim());
      const questAsync = []
      for (const quest of quests) {
        const [questId, body] = quest.split('||').map(data => data.trim())

        const url = `https://hub.beamable.network/modules/questsold/${questId}`
        headers["next-action"] = "7f63ca5a304b9b646d220b090c9a8b2346108e02e0"
        headers.Cookie = cookie
        questAsync.push(fetch(url, {
          method: 'POST',
          headers,
          agent,
          body
        }))
        logger(`Đang claim quest ${questId}`,)

      }
      await Promise.all(questAsync)
      logger("Đã claim tất cả các quest thêm mới.", "success")
  
    } catch (error) {
      logger(`Lỗi claim quest: ${error.message}`, 'error')
    }
}

async function checkProxySpeed(agent) {
  const startTime = Date.now();
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 5000);
  const testUrl = "https://icanhazip.com/"
  try {
      const response = await fetch(testUrl, {
          agent,
          signal: controller.signal,
      });

      clearTimeout(timeout);
      const elapsedTime = Date.now() - startTime;
      return {
          status: 'success',
          time: elapsedTime,
          statusCode: response.status,
      };
  } catch (error) {
      return {
          status: 'error',
          error: error.name === 'AbortError' ? 'Timeout' : error.message,
      };
  }
}

async function openBox(cookie, agent) {
  try {
    const url = 'https://hub.beamable.network/modules/profile/5456'
    headers.Cookie = cookie
    headers["next-action"] = "7f1ddd18727e2bda9884d4f73c1ed2de315c9667cf"
    await fetch(url, {
      method: 'POST',
      headers,
      agent,
      body: "[5456,{\"path\":\"/profile/5456\"},1]"
    })
    logger("Đã mở hộp daily", 'success')

  } catch (error) {
    logger(`Lỗi daily check-in: ${error.message}`, 'error')

  }
}

async function getNonce(cookie, agent) {
  const url = 'https://hub.beamable.network/modules/aprildailies';
  headers.Cookie = cookie;

  for (let attempt = 1; attempt <= 5; attempt++) {
    try {
      const request = await fetch(url, {
        method: 'GET',
        headers,
        agent,
      });

      const response = await request.text();
      const text = response.slice(-400000);
      const cleanedText = text.replace(/\\"/g, '"');
      const regex = /"nonce":"([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"/;
      const match = cleanedText.match(regex);

      if (match) {
        return match[1];
      } else {
        logger(`Không tìm thấy nonce (lần ${attempt})`, 'warn');
      }
    } catch (error) {
      logger(`Lỗi get nonce (lần ${attempt}): ${error.message}`, 'error');
    }

    if (attempt < 5) {
      // Đợi 5 giây trước khi thử lại
      await new Promise((resolve) => setTimeout(resolve, 5000));
    }
  }

  // Nếu sau 5 lần vẫn không thành công, trả về null hoặc throw error
  logger('Không thể lấy nonce sau 5 lần thử.', 'error');
  return null;
}

async function dailyCheckIn(cookie, agent, nonce) {
  try {
    const a = await fetch("https://hub.beamable.network/modules/aprildailies", {
      "headers": {
        "accept": "text/x-component",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "text/plain;charset=UTF-8",
        "next-action": "7fb84504b1af6fa4a015452e147da5ba17d2d03551",
        "next-router-state-tree": "%5B%22%22%2C%7B%22children%22%3A%5B%5B%22host%22%2C%22hub.beamable.network%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22modules%22%2C%7B%22children%22%3A%5B%5B%22moduleIdOrPath%22%2C%22aprildailies%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fmodules%2Faprildailies%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Herond\";v=\"120\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "cookie": cookie,
        "Referer": "https://hub.beamable.network/modules/aprildailies",
        "Referrer-Policy": "strict-origin-when-cross-origin"
      },
      "body": `[467,"${nonce}","aprildailies"]`,
      "method": "POST"
    });

    if (a.status == 200) {
      logger("Đã daily check-in thành công", 'success')
      await openBox(cookie, agent)
    }

    if (a.status == 403) {
      logger("Lỗi bị chặn do proxy nằm trong quốc gia bị chặn bởi dự án", 'error')
    }

    if (a.status == 504) {
      logger("Server của dự án đang quá tải, thử lại sau 5 phút", 'error')
      await new Promise(resolve => setTimeout(resolve, 5 * 60 * 1000))
      await dailyCheckIn(cookie, agent, nonce)
    }

  } catch (error) {
    logger(`Lỗi daily check-in: ${error.message}`, 'error')

  }
}

async function main() {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  console.log("TOOL ĐƯỢC PHÁT TRIỂN BỞI: THIEN THO TRAN");
  console.log(
    "Tham gia group facebook để nhận tool mới: https://www.facebook.com/groups/2072702003172443/"
  );
  console.log("------------------------------------------------------------");
  const doTask = await rl.question('Bạn có muốn làm task không, hay chỉ daily mỗi ngày? y/n: ');

  while (true) {
    const { proxies, cookies } = await readFiles();
    await Promise.all(cookies.map(async (cookie, i) => {
      logger(`Đang thực hiện tài khoản thứ ${i + 1}`)
      let agent = null;
      if (proxies[i]) {
        agent = new HttpsProxyAgent(proxies[i])
        logger(`Đang kiểm tra proxy ${proxies[i]}`)
        const checkProxy = await checkProxySpeed(agent);
        console.log(`Proxy: ${proxies[i]} - Tốc độ: ${checkProxy.time}ms - Status: ${checkProxy.statusCode}`);
      }
      const nonce = await getNonce(cookie, agent)

      if (doTask === 'y') {
        await clickQuest(cookie, agent, nonce)
        logger("Chờ 1 chút để claim", 'warn')
        await new Promise(resolve => setTimeout(resolve, 10 * 1000))
        await completeQuest(cookie, agent, nonce)
      }
  
      await dailyCheckIn(cookie, agent, nonce)
    }))

    logger("Chờ 6 tiếng để tiếp tục daily", 'warn')

    await new Promise(resolve => setTimeout(resolve, 6 * 60 * 60 * 1000))
  }
}

main();

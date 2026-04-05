const ytSearch = require('yt-search');
const fs = require('fs');
const path = require('path');

const draftsDir = path.join(__dirname, '../drafts');
const outputJson = path.join(__dirname, 'youtube_mappings.json');

async function main() {
    const drafts = fs.readdirSync(draftsDir, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);
        
    const mappings = {};
    
    for (const slug of drafts) {
        // Construct a highly relevant YouTube search query based on slug keywords
        let query = slug.replace(/-/g, ' ');
        if (query.includes('kling')) {
            query = "Kling AI hướng dẫn sử dụng";
        } else if (query.includes('sora')) {
            query = "Sora OpenAI review đánh giá";
        } else if (query.includes('veo')) {
            query = "Google Veo 3 review";
        } else if (query.includes('tiktok') || query.includes('ngan')) {
            query = "Làm video TikTok bằng AI hướng dẫn";
        } else if (query.includes('anh-tinh-den-video')) {
            query = "Biến ảnh thành video AI";
        } else if (query.includes('lam-video-ai-tu-dong')) {
            query = "Workflow tạo video AI tự động";
        } else {
            query = "Tạo video bằng AI 2025 " + query;
        }
        
        console.log(`[${slug}] Searching YT for: "${query}"`);
        try {
            const r = await ytSearch(query);
            const videos = r.videos.slice(0, 5).map(v => v.videoId);
            mappings[slug] = videos;
            console.log(`[${slug}] Found IDs:`, videos);
        } catch (err) {
            console.error(`[${slug}] Error:`, err.message);
        }
        
        // Wait 1s to prevent rate limiting
        await new Promise(res => setTimeout(res, 1000));
    }
    
    fs.writeFileSync(outputJson, JSON.stringify(mappings, null, 2));
    console.log(`Written to ${outputJson}`);
}

main();

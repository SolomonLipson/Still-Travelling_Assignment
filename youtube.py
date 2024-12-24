import requests
import pandas as pd

class YouTubeDataScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def get_videos_for_genre(self, genre, max_results=500):
        """
        Fetches videos related to a genre from YouTube API
        """
        videos = []
        next_page_token = None
        while len(videos) < max_results:
            url = f"{self.base_url}/search"
            params = {
                "part": "id,snippet",
                "q": genre,
                "type": "video",
                "maxResults": min(50, max_results - len(videos)),
                "pageToken": next_page_token,
                "key": self.api_key
            }
            response = requests.get(url, params=params)
            if response.status_code != 200:
                print(f"Error fetching videos: {response.text}")
                break
            response_json = response.json()
            videos.extend(response_json.get('items', []))
            next_page_token = response_json.get("nextPageToken")
            if not next_page_token:
                break
        return videos

    def get_video_details(self, video_ids):
        """
        Fetches detailed information of videos using their IDs
        """
        url = f"{self.base_url}/videos"
        params = {
            "part": "snippet,statistics,contentDetails,topicDetails",
            "id": ",".join(video_ids),
            "key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching video details: {response.text}")
            return []
        return response.json().get("items", [])

    def get_video_captions(self, video_id):
        """
        Fetches captions for a specific video ID
        """
        url = f"{self.base_url}/captions"
        params = {
            "videoId": video_id,
            "key": self.api_key
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error fetching captions: {response.text}")
            return None
        
        captions = response.json().get('items', [])
        if captions:
            caption_id = captions[0]['id']
            caption_url = f"{self.base_url}/captions/{caption_id}"
            caption_response = requests.get(caption_url, params={'key': self.api_key})
            if caption_response.status_code == 200:
                return caption_response.text
        return None

    def scrape_youtube_data(self, genre):
        """
        Scrapes YouTube data for a specific genre
        """
        video_data = []
        videos = self.get_videos_for_genre(genre)
        for i in range(0, len(videos), 50):
            video_ids = [video['id']['videoId'] for video in videos[i:i+50]]
            details = self.get_video_details(video_ids)
            for detail in details:
                snippet = detail["snippet"]
                statistics = detail.get("statistics", {})
                content = detail["contentDetails"]
                video_id = detail["id"]
                caption_text = self.get_video_captions(video_id)
                captions_available = bool(caption_text)
                
                video_data.append({
                    "Video URL": f"https://www.youtube.com/watch?v={video_id}",
                    "Title": snippet["title"],
                    "Description": snippet["description"],
                    "Channel Title": snippet["channelTitle"],
                    "Keyword Tags": ", ".join(snippet.get("tags", [])),
                    "Category": snippet.get("categoryId"),
                    "Topic Details": detail.get("topicDetails", {}).get("topicCategories", []),
                    "Published at": snippet["publishedAt"],
                    "Video Duration": content["duration"],
                    "View Count": statistics.get("viewCount", 0),
                    "Comment Count": statistics.get("commentCount", 0),
                    "Captions Available": captions_available,
                    "Caption Text": caption_text if captions_available else "",
                })
        return video_data

class CSVExporter:
    def __init__(self, filename):
        self.filename = filename

    def save_to_csv(self, data, columns_order):
        """
        Saves the scraped data to a CSV file with the specified column order
        """
        df = pd.DataFrame(data, columns=columns_order)
        df.to_csv(self.filename, index=False)
        print(f"CSV generated successfully at {self.filename}")

def main():
    # User input for genre
    genre = input("Enter the genre: ")

    # API Key for YouTube API
    api_key = "AIzaSyDCFtkItHA0c-Pq2DDFG9LcFTkTo7yVs0U"  # Replace with your actual API key

    # Initialize YouTubeDataScraper and CSVExporter
    scraper = YouTubeDataScraper(api_key)
    exporter = CSVExporter("youtube_data.csv")

    # Scrape the data from YouTube
    data = scraper.scrape_youtube_data(genre)

    columns_order = [
        "Video URL", "Title", "Description", "Channel Title", "Keyword Tags", 
        "Category", "Topic Details", "Published at", "Video Duration", 
        "View Count", "Comment Count", "Captions Available", "Caption Text"
    ]

    # Save the data to CSV
    exporter.save_to_csv(data, columns_order)

if __name__ == "__main__":
    main()

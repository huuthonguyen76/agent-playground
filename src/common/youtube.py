from youtube_transcript_api import YouTubeTranscriptApi, FetchedTranscript
from typing import List


def get_youtube_transribe(video_id: str) -> List[FetchedTranscript]:
    client = YouTubeTranscriptApi()
    transcript = client.fetch(video_id).to_raw_data()

    l_transcript = [
        ele['text'] for ele in transcript
    ]

    return ' '.join(l_transcript)


if __name__ == '__main__':
    print(get_youtube_transribe('aXiOBAXYxCI'))

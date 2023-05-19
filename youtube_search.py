from googleapiclient.discovery import build

api_key = 'AIzaSyBLp6nbESLvQhz1qEGp0kOcbJ9o0AMjUi4'
youtube = build('youtube', 'v3', developerKey=api_key)

try:
    
    keywords = input("Enter the search keywords: ")

    num_results = int(input("Enter the number of search results: "))

    search_response = youtube.search().list(
        part='snippet',
        q=keywords,
        type='video',
        maxResults=num_results
    ).execute()

    print(f"Results for search keywords: '{keywords}'")
    print('-----------------------------')

    for search_result in search_response.get('items', []):
        title = search_result['snippet']['title']
        video_id = search_result['id']['videoId']
        link = f'https://www.youtube.com/watch?v={video_id}'

        print('Title:', title)
        print('Link:', link)
        print('')

    print('-----------------------------')

except Exception as e:
    print('An error occurred:', str(e))

finally:
    print('Search completed!')

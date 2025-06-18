import boto3

def main():
    client = boto3.client('rekognition', region_name='eu-central-1')
    s3_bucket = 'rekognition-demo-bucket1923'

    action = input("What would you like to do? (upload/identify): ").strip().lower()

    if action == 'upload':
        image_names = input("Enter the names of the images to upload (comma-separated): ").split(',')
        image_names = [name.strip() for name in image_names]

        for image_name in image_names:
            image_id = input(f"Enter an ID for the image '{image_name}': ").strip()
            try:
                response = client.index_faces(
                    CollectionId='my-face-collection',
                    Image={'S3Object': {'Bucket': s3_bucket, 'Name': image_name}},
                    ExternalImageId=image_id,
                    DetectionAttributes=['DEFAULT']
                )
                print(f"Face added with ID: {image_id} for image '{image_name}'")
            except client.exceptions.InvalidS3ObjectException:
                print(f"Error: The image '{image_name}' could not be accessed in S3. Please check the object key and permissions.")
            except Exception as e:
                print(f"An unexpected error occurred for image '{image_name}': {e}")

    elif action == 'identify':
        image_names = input("Enter the names of the images to identify (comma-separated): ").split(',')
        image_names = [name.strip() for name in image_names]

        for image_name in image_names:
            try:
                response = client.search_faces_by_image(
                    CollectionId='my-face-collection',
                    Image={'S3Object': {'Bucket': s3_bucket, 'Name': image_name}},
                    MaxFaces=1,
                    FaceMatchThreshold=90
                )
                if response['FaceMatches']:
                    for match in response['FaceMatches']:
                        print(f"Match found for image '{image_name}': ID - {match['Face']['ExternalImageId']}, Similarity - {match['Similarity']:.2f}%")
                else:
                    print(f"No matching face found for image '{image_name}'.")
            except Exception as e:
                print(f"An unexpected error occurred for image '{image_name}': {e}")
    else:
        print("Invalid option. Please choose 'upload' or 'identify'.")

if __name__ == "__main__":
    main()
import video_process as vp
import image_process as ct
import image_reco as reco
import text_process as txt
import os
import cv2


def main():
    # =================== 동영상 테스트 ================================
    fianl_result_array = []
    section_result_array = []
    hightlight_result_array = []

    video_path = 'test_video/ten.mp4'
    # video에서 프레임 추출 
    frame_images = vp.extract_frame_from_video(video_path)
    # 추출된 프레임에서 글자 영역 찾기

    for i, frame in enumerate(frame_images):
        vp.save_image(ct.get_gray(frame), 'frames/frame_{}.jpg'.format(i))
        final_result = []
        copy = frame.copy()

        cropped_images = ct.image_all_process(copy)[1]
        num = 0
        # 한 프레임의 글자 영역들의 텍스트 추출 
        # 자막들 
        for con in cropped_images["contours"]:
            # 프레임에서 추출한 영역들 저장 
            ct.save_crooped_contours(con, 'contours/contours_{}'.format(num))
            # 영역들에서 글자 추출 
            result = reco.extract_text(con)
            #         # 추출된 글자 전처리 후 임시 보관
            tmp = txt.text_pre_process(result)
            if (tmp is not None):
                final_result.append(tmp)
            # final_result.append(result)
            num += 1
        # 한 프레임 씩 배열에 저장 
        fianl_result_array.append(final_result)

        # 섹션 
        # 섹션 영역 저장
        ct.save_crooped_contours(cropped_images["section"], 'sections/section_{}'.format(i))
        # 섹션에서 글자 추출 
        section = reco.extract_text(cropped_images["section"])
        # 추출된 글자 전처리 후 저장 
        section_result_array.append(txt.text_pre_process(section))
        # section_result_array.append(section)

    # 모든 결과 값들 저장 하기 
    txt.text_save(fianl_result_array, section_result_array, 'result.csv')

#list.txt 파일에 "file 'video_clip{}.mp4'"의 값을 추가
#a 에 하이라이트 추출 값이 들어가면 됨
list= r"C:\Users\user\PycharmProjects\ai_highlight_soccer"

while hightlight_result_array.len:
    for i in hightlight_result_array:
        with open (list, 'a') as f:
            f.write("file 'video_clip{}.mp4'\r\n")
        os.system("ffmpeg -i Fullvideo.mp4 -ss {a} -to {a} -c copy video_clip{}.mp4")

#list에 있는 하이라이트 비디오 를 모두 통합한다.
os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy highlightvideo.mp4")



if __name__ == "__main__":
    main()
    # vision_test('output/frames/frame308.jpg')


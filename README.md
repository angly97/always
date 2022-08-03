# :dog: 또바기: 언제나 한결같이, 꼭 그렇게



## Description

![all](https://user-images.githubusercontent.com/70613905/162095645-1846fd0b-0a13-455c-85cd-15d69fc5b5db.png)


 * 하늘나라에 있는 반려동물에게 편지를 보낸다는 컨셉의 반려동물 추모 서비스
 * 기능
   * 동물 등록/조회/삭제
     * 등록: 사용자가 받는 동물 이름, 사진, 정보, 전하고 싶은 말 등을 기입하는 편지 형식으로 반려동물을 등록
     * 조회: 검색을 하거나, 카테고리 게시판을 통해 조회하고 싶은 특징을 가진 동물 조회
     * 삭제: 나의 편지함(= 마이페이지)에서 사용자가 등록한 동물 삭제
   * 메시지 보내기
     * 해당 동물의 페이지에 방명록 형식으로 메시지를 남김
   * 반려동물 장례 장소 검색
     * Kakao map API를 통해 반려동물 장례를 하는 장소의 정보를 얻음
 * 개발 프레임워크
   * Django
     * 선택한 이유
        * 프로젝트 생성 시, MVT패턴이 자동으로 적용되고, 웹에서 공통적으로 쓰이는 기능이 내장되어 있어서, 웹 개발을 처음으로 공부하기에 적합하다고 생각
        * 풀스택 프레임워크라 프론트 관련 프레임워크(React, Vue 등)없이 만들 수 있었음
        * 자체 ORM을 제공해서, ORM에 대한 경험도 쌓을 수 있음

## Requirement

* Python 2.7 or higher
* Django



## Test

```bash
# run server
python manage.py runserver
```


## Study

* [Django 학습 정리 노트] https://github.com/angly97/webstudy_note
- 파이썬 기반 웹 개발 프레임워크

  - 라이브러리보다 더 구성이 되어있어서 개발 속도 더 빠름

- MVT 모델

  - Model (= Model)
    - 데이터베이스
    - model.py

  - View (= Controller)
    - Model과 Template을 연결
    - url에 따라 동작해야하는 함수들 정의
    - urls.py의 요청을 토대로 model 데이터 작업하여 template에 넘김 or template의 데이터를 작업하여 model에 적용

  - Template (= View)
    - 화면을 보여주는 인터페이스

- 장점

  - 대부분의 웹에서 공통적으로 쓰이는 기능이 이미 구현되어 있음 => 개발 시간 단축

    - 로그인, 회원가입, 인증, CORS, data parsing 등

  - 풀스택 프레임워크라서 => 프론트 관련 프레임워크(React, Vue 등) 없이 만들 수 있음

  - ORM 제공

    - 객체와 관계형 데이터베이스를 매핑

    - DB 테이블을 클래스로 관리하는 등 객체지향적인 개발 가능

      ```python
      from django.db import models
      from user.models import User
      
      class Company(models.Model):
          id = models.IntegerField(primary_key=True)
          name = models.CharField(max_length=50)
          # CACADE 설정하면 select_related 시, inner_join
          owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
          # SET_NULL 설정하면 해당 User 객체 삭제 시, Null로 변하기 때문에 Join이 안되는 것을 반지하고자, left join으로 자동 수행됨
          owner_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
          photo = models.ImageField(upload_to='/photo', null=True)
          introduce = models.TextField()
          date = models.DateField()
      ```

      ```python
      # select * from Company : objects.all()
      companies = Company.objects.all()
      
      # select * from Company where ~ : objects.get(), objects.filter(), objects.exclude()
      company = Company.objects.get(name='abc')
      companies = Company.objects.filter(category='it', since=100)
      companies = Company.objects.exclude(category='it')	# not
      
      # insert : objects.create
      Company.objects.create(name='abc', category='it', since=50)
      
      company = Company()
      company.name = 'abc' ...
      company.save()
      
      
      # delete : 변수.delete()
      company = Company.objects.get(name='abc')
      company.delete()
      
      # join : selected_related()
      company = Company.objects.filter(category='id').select_related('owner_id')
      
      
      # 새로운 추가 쿼리 : prefetched_related('변수명'|'클래스_set')
      # SELECT * FROM User
      # SELECT * FROM Company WHERE owner_id IN (첫번째 쿼리 결과 id 리스트)
      companies = User.objects.prefetched_related('company_id')
      companies = User.objects.prefetched_related('Company_set')
      
      
      # A에서 B를 참조하고 싶다면,
      # SELECT * FROM Company INNER/LEFT JOIN User ON owner_id = user_id
      # SELECT * FROM User WHERE user_id IN (첫번째 쿼리 결과 id 리스트)
      company = Company.object.select_related('owner_id').prefetch_related('역방향 참조 필드명')
      ```

      - selected_related()

        →   A:B == 1:n, B에서 A참조 시 사용 (정방향 참조만 가능)

        →   관계된 테이블까지 한 번의 쿼리로 가져옴

        →   불러온 data는 DB 서버 종료 전까지 캐시에 남아 매 쿼리마다 DB에 접근 안해도 됨 => DB 접근 빈도 줄일 수 있음

        →   on_delete=models.**CASCADE** : INNER JOIN

        →   on_delete=models.**SET_NULL** : LEFT JOIN

      - prefetched_related()

        →   A:B == n:m, A <=> B참조 시 사용 (정/역방향 참조)

        ​	(cf. 역참조 = 해당 객체를 참조하는 객체 데이터 가져오는 경우)

        →   쿼리를 한 번 더 실행시킴

        →   불러온 데이터 캐시에 저장

  - serializer

    - 모델 인스턴스 같은 복잡한 데이터를 JSON, XML 등 다른 유형으로 쉽게 변환
    - 데이터 유효성 검사 후, 다른 타입으로 형변환

  - 어드민 패널

    - DB에 CRUD 할수 있는 UI 제공

- 단점

  - 파이썬의 단점

    - 인터프리터 언어라 생기는 문제

      →   속도

      →   실행될 때까지 걸리지 않는 에러

  - 구현되어 있는 것이 많고, 구조가 정해져 있어서 유연성이 떨어짐

  - 성능이 다른 웹 개발 프레임워크(Node.js 등)보다 좋지 못함





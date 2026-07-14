# 배포 안내

이 프로젝트를 GitHub에 푸시하면 자동으로 정적 사이트가 생성되어 `gh-pages` 브랜치로 배포됩니다.

1) 원격 리포지토리에 푸시

```bash
git add .
git commit -m "Add site and deploy workflow"
git push origin main
```

2) GitHub Actions 실행 후 배포 확인
- Actions 탭에서 `Deploy to GitHub Pages` 워크플로 실행 로그 확인
- 배포 성공 시 기본 URL(퍼블릭 리포지토리 기준):

  https://gube0121.github.io/re/

3) 커스텀 도메인 사용 시 `CNAME` 파일을 `site-dist`에 추가하거나 GitHub Pages 설정에서 도메인을 연결하세요.

문제가 발생하면 로그와 함께 알려주시면 설정·디버그 도와드리겠습니다.

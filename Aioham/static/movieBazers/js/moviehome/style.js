var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
  
  
  //show video
  
  let playButton=document.querySelector('.play-movie');
  let video=document.querySelector('.video-container');
  let myvideo=document.querySelector("#myvideo")
  let closebtn=document.querySelector('.close-video');
  
  playButton.onclick=()=>{
    video.classList.add("show-video");
    // auto play when click on button
    myvideo.play()
  };
  
  closebtn.onclick=()=>{
    video.classList.remove("show-video");
    // pause on close video
    myvideo.pause();
  };
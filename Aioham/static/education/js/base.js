
// nav scrolling 
window.addEventListener('scroll',()=>{
    document.querySelector('nav').classList.toggle('window-scroll',window.scrolly>0)
})


// show/hide faq answer

const faqs = document.querySelectorAll('.faq');

faqs.forEach(faq=>{
    faq.addEventListener('click',()=>{
        faq.classList.toggle('open');
        // change icon 
        const icon=faq.querySelector('.faq_icon i');
        if(icon.className=== 'uil uil-plus'){
            icon.className = 'uil uil-minus'
        }else{
            con.className = 'uil uil-plus'
        }
    })
})
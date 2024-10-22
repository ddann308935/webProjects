document.addEventListener("DOMContentLoaded", function() {​

    const lazyImages = document.querySelectorAll("img[data-src]");​
  
    function lazyLoad() {​
  
      lazyImages.forEach(img => {​
  
        if (img.getBoundingClientRect().top < window.innerHeight && 
        img.getBoundingClientRect().bottom > 0 && getComputedStyle(img).display 
        !== "none") 
        {​
          img.src = img.getAttribute("data-src");​
          
          img.removeAttribute("data-src");​
        }​
  
      });​
  
    }​
  
    window.addEventListener("scroll", lazyLoad);​
  
    lazyLoad(); // Load visible images on page load​
  
  });
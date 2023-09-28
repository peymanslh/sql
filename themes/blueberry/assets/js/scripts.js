(function() {
  let navItems = document.getElementsByClassName("nav-item");
  for (let item of navItems) {
    item.addEventListener("click", activeTab);
  }
})();

function activeTab(e) {
  e.preventDefault();
  e.target.classList.add("active");
  const contentID = e.target.getAttribute("href").replace("#", "");
  getSiblings(e.target).forEach(el => {
    el.classList.remove("active");
  })
  const content = document.getElementById(contentID);
  getSiblings(content).forEach(el => {
    el.classList.remove("active");
  })
  content.classList.add("active");
}

function getSiblings (e) {
  let siblings = [];
  if (!e.parentNode) {
    return siblings;
  }
  let sibling = e.parentNode.firstChild;
  while (sibling) {
    if (sibling.nodeType === 1 && sibling !== e) {
      siblings.push(sibling);
    }
    sibling = sibling.nextSibling;
  }
  return siblings;
};

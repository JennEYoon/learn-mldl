window.livbookVendorErrorFallback = function(){
    window.hasLivebookVendorLoadingErrors = true;
};

window.handleLivebookAppLoadingError = function(){
    var startOfBookPathIndex = document.location.href.indexOf("/book/");
    
    document.body.classList.remove("not-loaded");
    
    if(startOfBookPathIndex != -1){ 
        loadBookFallback(startOfBookPathIndex);
        return;
    }

    var startOfCatalogPathIndex = document.location.href.indexOf("/catalog");
    if(startOfCatalogPathIndex != -1){
        loadCatalogFallback(startOfCatalogPathIndex);
        return;
    }

    loadLandingPageFallback();
};

function loadLandingPageFallback(){
    var baseServerUrl = (document.location.href.indexOf("livebook.manning.com") != -1 
                        ? "https://vbook.manning.com/" : "https://vbook-qa.manning.com/");
    var mainPageContentContainer = document.getElementById("main-page-content");
    mainPageContentContainer.innerHTML = "<div class='landing-page-fallback-container'><h2>bestsellers</h2><div class='landing-page-fallback-bestsellers-container'></div><h2>categories</h2><div class='landing-page-fallback-catalog-container'></div></div>";

    var bestsellersRequest = new XMLHttpRequest();
    bestsellersRequest.addEventListener("load", function(data){
        showBestsellersFallback(JSON.parse(this.responseText));
    });

    var catalogRequest = new XMLHttpRequest();
    catalogRequest.addEventListener("load", function(data){
        showLandingPageCatalogFallback(JSON.parse(this.responseText));
    });

    bestsellersRequest.open("GET", baseServerUrl + "api/catalog/getBestsellers");
    bestsellersRequest.send();

    catalogRequest.open("GET", baseServerUrl + "api/catalog/getCatalog");
    catalogRequest.send();
}

function showBestsellersFallback(bestsellers){
    var html = "";
    var imageBaseUrl = "https://images.manning.com/180/225/resize/"

    for(var i = 0; i < bestsellers.length; i++){
        var bestseller = bestsellers[i];                   
        html += "<a class='bestseller-fallback-image' href='" + ("/#!/book/" + bestseller.slug) + "'>" + "<img src='" + (imageBaseUrl + bestseller.imageUrl) + "' alt='" + bestseller.title + "'/></a>";
    }

    var bestellersFallbackContainer = document.querySelector(".landing-page-fallback-bestsellers-container");
    if(bestellersFallbackContainer != null){
        bestellersFallbackContainer.innerHTML = html;
    }
}

function showLandingPageCatalogFallback(catalog){
    var html = "";
    var allCategoriesMap = {}; 

    for(var i = 0; i < catalog.length; i++){
        var book = catalog[i];
        var categories = (book.categories || "").split(";");
        for(var j = 0; j < categories.length; j++){
            var category = categories[j];
            allCategoriesMap[category] = true;
        }
    }

    for(var category in allCategoriesMap){
        if(category){
            html += "<a class='catalog-category-fallback-link' href='/#!/catalog/" + category + "'>" + category + "</a>";
        }
    }

    var catalogFallbackContainer = document.querySelector(".landing-page-fallback-catalog-container");
    if(catalogFallbackContainer != null){
        catalogFallbackContainer.innerHTML = html;
    }
}

function loadCatalogFallback(startOfCatalogPathIndex){
    var category = document.location.href.substr(startOfCatalogPathIndex).replace("/catalog", "").toLowerCase();
    if(category.indexOf("/") == 0){
        category = category.substr(1);
    }
    var baseServerUrl = (document.location.href.indexOf("livebook.manning.com") != -1 
                        ? "https://vbook.manning.com/" : "https://vbook-qa.manning.com/");


    var catalogRequest = new XMLHttpRequest();
    catalogRequest.addEventListener("load", function(data){
        var catalog = JSON.parse(this.responseText);
        var categoryBooksHtml = [];

        for(var i = 0; i < catalog.length; i++){
            var book = catalog[i];
            if(!category){
                category = book.categories.toLowerCase().split(";")[0] || "javascript";
            }
            
            if(book.categories.toLowerCase().indexOf(category) >= 0){
                categoryBooksHtml.push("<li><a href='/#!/book/" + book.slug + "'>" + book.title + "</a></li>");
            }
        }

        var mainPageContentContainer = document.getElementById("main-page-content");
        mainPageContentContainer.innerHTML = "<ul>" + categoryBooksHtml.join("") + "</ul>";
    });

    catalogRequest.open("GET", baseServerUrl + "api/catalog/getCatalog");
    catalogRequest.send();
}

function loadBookFallback(startOfBookPathIndex){
    var path = document.location.href.substr(startOfBookPathIndex).replace("/book/", "");
    var firstSlashIndex = path.indexOf("/");
    var bookShortNameOrSlug = "";
    var bookElementShortName = ""
    
    if(firstSlashIndex == -1){
        bookShortNameOrSlug = path;
    }
    else {
        bookShortNameOrSlug = path.substr(0, firstSlashIndex);
        path = path.substr(firstSlashIndex + 1);
        var secondSlashIndex = path.indexOf("/");
        bookElementShortName = secondSlashIndex == -1 ? path : path.substr(0, secondSlashIndex);
    }

    if(bookShortNameOrSlug){
        livebookErrorLoadBookElement(bookShortNameOrSlug, bookElementShortName);
    }
}

function livebookErrorLoadBookElement(bookShortNameOrSlug, bookElementShortName){
    var bookDataRequest = new XMLHttpRequest();
    bookDataRequest.addEventListener("load", function(){
        var response = JSON.parse(this.responseText);
        if(response.book && response.bookElement){
            var book = response.book;
            var bookElement = response.bookElement;
            var nextBookElement = response.nextBookElement;
            var previousBookElement = response.previousBookElement;
            var title = bookElement.title + " - " + book.title;
            document.title = title;

            var imagesRoot = (document.location.href.indexOf("livebook.manning.com") != -1 
                            ? "https://dpzbhybb2pdcj.cloudfront.net" 
                            : "https://dhjb9cmbg5852.cloudfront.net");

            var coverUrl = imagesRoot + "/" + book.shortName + "/Figures/cover.jpg";

            if(bookElement.contentUrl){
                var bookElementContentRequest = new XMLHttpRequest();
                bookElementContentRequest.addEventListener("load", function(){
                    var bookElementHTML = this.responseText.replace(/\{\{BOOK_ROOT_FOLDER\}\}/g, imagesRoot);
                    
                    var mainPageContentElement = document.getElementById("main-page-content");
                    mainPageContentElement.innerHTML = '<div class="row" id="book-content-main-row">'
                                                        + '<div class="large-12 columns">'
                                                            + '<div id="book-main-content-container">'
                                                                + '<div id="book-markup-container" class="fallback-book-markup-container" style="padding-top: 50px;">'
                                                                    + bookElementHTML
                                                                + '</div>'
                                                            + '</div>'
                                                        + '</div>'
                                                     + '</div>';
                    updateMetaContent();
                    updateMetaImages(coverUrl);
                });
                bookElementContentRequest.open("GET", bookElement.contentUrl);
                bookElementContentRequest.send();
            }

            var previousElementLink = document.querySelector("#footer .previous-element-link");
            var nextElementLink = document.querySelector("#footer .next-element-link");

            
            previousElementLink.setAttribute("href", previousBookElement.link);
            nextElementLink.setAttribute("href", nextBookElement.link);
            
            previousElementLink.classList.remove("invisible");
            nextElementLink.classList.remove("invisible");
        }
    });
    bookDataRequest.open("GET", (document.location.href.indexOf("livebook.manning.com") != -1 
                    ? "https://vbook.manning.com/" : "https://vbook-qa.manning.com/")
                    + "api/book/getBookElement?bookShortNameOrSlug=" + bookShortNameOrSlug + "&bookElementShortName=" + bookElementShortName);
    bookDataRequest.send();
}

function updateMetaContent(){
    try {
        var introductionSummaryItems = document.querySelectorAll(".introduction-summary li");
        var summary = "";
        for(var i = 0; i < introductionSummaryItems.length; i++){
            summary += introductionSummaryItems[i].textContent + "; ";
        }

        if(summary){
            var metaContentTags = document.querySelectorAll(".meta-description");
            for(var i = 0; i < metaContentTags.length; i++){
                metaContentTags[i].setAttribute("content", summary);
            }
        }
    }
    catch(e){}
}

function updateMetaImages(bookCover){
    try {
        if(bookCover){
            var metaContentTags = document.querySelectorAll(".meta-description");
            for(var i = 0; i < metaContentTags.length; i++){
                metaContentTags[i].setAttribute("content", bookCover);
            }
        }
    }
    catch(e){}
}
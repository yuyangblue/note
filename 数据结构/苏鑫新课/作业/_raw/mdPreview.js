    /**
        * 自定义一个语法，识别形如 ***ABC*** 的内容，并将其替换成 <span style="color: red"><strong>ABC</strong></span>
        */
        var CustomHookA = Cherry.createSyntaxHook('important', Cherry.constants.HOOKS_TYPE_LIST.SEN, {
            makeHtml(str) {
                return str.replace(this.RULE.reg, function(whole, m1, m2) {
                    return `<span style="color: red;"><strong>${m2}</strong></span>`;
                });
            },
            rule(str) {
                return { reg: /(\*\*\*)([^\*]+)\1/g };
            },
        });
        
        var CustomHookRawInline = Cherry.createSyntaxHook('rawInline', Cherry.constants.HOOKS_TYPE_LIST.SEN, {
            makeHtml(str) {
               
                return str.replace(this.RULE.reg, function(whole, m1, m2) {
                    return `${m2}`;
                });
            },
            rule(str) {
                const regex = {
                    begin: '@@(cghtml)\\{',
                    end: '\\}@@',
                    content: '([\\s\\S]*?)'
                };
                regex.reg = new RegExp(regex.begin + regex.content + regex.end, 'g');
                return regex;
              },
        });
        
        var CustomHookRawBlock = Cherry.createSyntaxHook('rawBlock', Cherry.constants.HOOKS_TYPE_LIST.PAR, {
            needCache: true, // 表明要使用缓存，也是实现排他的必要操作
            makeHtml(str) {
                const that = this;
                return str.replace(this.RULE.reg, function(whole, m1) {
                  const result = `\n<div style="border: 1px solid;border-radius: 15px;background: gold;">${m1}</div>\n`;
                  console.log(result);
                    return that.pushCache(result); // 将结果转成占位符
                });
            },
            rule(str) {
                const regex = {
                    begin: '^@@@\\s*',
                    end: '\\s*@@@',
                    content: '([\\s\\S]*?)'
                };
                regex.reg = new RegExp(regex.begin + regex.content + regex.end, 'g');
                return regex;
              },
        });

    var cherryConfig = {
        id: 'cgpreviewmarkdown',
        externals: {
          echarts: window.echarts,
          katex: window.katex,
          MathJax: window.MathJax,
        },
        engine: {
          global: {
            urlProcessor(url, srcType) {
              console.log(`url-processor`, url, srcType);
              return url;
            },
            htmlWhiteList: 'iframe|script|style',
          },
          syntax: {
            fontEmphasis: {
              allowWhitespace: true, // 是否允许首尾空格
            },
            mathBlock: {
              engine: 'katex', // katex或MathJax
              src: '', ///includes/cherrymd/dep/tex-svg.js 如果使用MathJax将js在此处引入，katex则需要将js提前引入
            },
            inlineMath: {
              engine: 'katex', // katex或MathJax
            },
            emoji: {
              useUnicode: false,
              customResourceURL: 'https://github.githubassets.com/images/icons/emoji/unicode/${code}.png?v8',
              upperCase: true,
            },
            // toc: {
            //     tocStyle: 'nested'
            // }
            // 'header': {
            //   strict: false
            // }
          },
          customSyntax: {
            // SyntaxHookClass
            rawInlineHook: {
                syntaxClass: CustomHookRawInline, // 将自定义语法对象挂载到 importHook.syntaxClass上
                force: false, // true： 当cherry自带的语法中也有一个“importHook”时，用自定义的语法覆盖默认语法； false：不覆盖
                before: 'fontEmphasis', // 定义该自定义语法的执行顺序，当前例子表明在加粗/斜体语法前执行该自定义语法
            },
            rawBlockHook: {
                syntaxClass: CustomHookRawBlock, // 将自定义语法对象挂载到 importHook.syntaxClass上
                force: false, // true： 当cherry自带的语法中也有一个“importHook”时，用自定义的语法覆盖默认语法； false：不覆盖
                before: 'blockquote', // 定义该自定义语法的执行顺序，当前例子表明在加粗/斜体语法前执行该自定义语法
            },
          },
        },
        toolbars: {
          toolbar: false,
          // 配置目录
          toc: {
            updateLocationHash: false, // 要不要更新URL的hash
            defaultModel: 'full', // pure: 精简模式/缩略模式，只有一排小点； full: 完整模式，会展示所有标题
            position: 'fixed', // 悬浮目录的悬浮方式。当滚动条在cherry内部时，用absolute；当滚动条在cherry外部时，用fixed
            cssText: 'right: 20px;',
            showAutoNumber: false,
          },  
        },
        editor: {
            id: 'cghackremove', // textarea 的id属性值
            name: 'cghackremove', // textarea 的name属性值
          defaultModel: 'previewOnly',
        },
        callback: {
          onClickPreview: function(e) {
            const {target} = e;
            if(target.tagName === 'IMG') {
              console.log('click img', target);
              const tmp = new Viewer(target, {
                  button: false,
                  navbar: false,
                  title: [1, (image, imageData) => `${image.alt.replace(/#.+$/, '')} (${imageData.naturalWidth} × ${imageData.naturalHeight})`],
                  hidden(){
                    tmp.destroy()
                  },
                });
              tmp.show();
            }
          }
        },
        previewer: {
            enablePreviewerBubble: false
          // 自定义markdown预览区域class
          // className: 'markdown'
        },
         keydown: [],
            //extensions: [],
    };


    function cgRenderMarkdownByValue(value, showtoc, containerID){
        if(arguments.length== 1){ 
            
            var config = Object.assign({}, cherryConfig, { value: value });
            var cherryPreview = new Cherry(config);
            
        }
        if(arguments.length== 2){ 
            var toolbarConfig = Object.assign({}, cherryConfig.toolbars, { toc: showtoc});           
            
            var config = Object.assign({}, cherryConfig, { value: value, toolbars: toolbarConfig });
            var cherryPreview2 = new Cherry(config);
            
        }
        if(arguments.length== 3){ 
            var toolbarConfig = Object.assign({}, cherryConfig.toolbars, { toc: showtoc});
           
            var config = Object.assign({}, cherryConfig, { value: value, toolbars: toolbarConfig, id: containerID });
            var cherryPreview3 = new Cherry(config);
        }
    }
    
    ////删除渲染后增加的textarea和大量的hidden元素
    function cgRemoveCherryMarkdownTrash(containerID){
        const previewMDContent = document.getElementById(containerID);
        if (!previewMDContent) return;

        const removeTargets = () => {
            previewMDContent.querySelectorAll('.cherry-editor--hidden').forEach(el => el.remove());

            const cherryHiddenNodes = previewMDContent.querySelectorAll('[class*="cherry-"]');
            cherryHiddenNodes.forEach(el => {
                const s = window.getComputedStyle(el);
                if (s.display === "none") {
                    el.remove();
                }
            });
        };

        // 先执行一次
        removeTargets();
        
        // 监控 DOM 变化（工具栏 dropdown 会重新创建）
        const observer = new MutationObserver(() => removeTargets());
        observer.observe(previewMDContent, { childList: true, subtree: true });
        
        /////
    }
    
    function cgRenderMarkdown(mkdocKey, showtoc, containerID){
        if(arguments.length== 1){ 
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, cherryConfig, { value: value });
                var cherryPreview = new Cherry(config);
            });
        }
        if(arguments.length== 2){ 
            var toolbarConfig = Object.assign({}, cherryConfig.toolbars, { toc: showtoc});           
            
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, cherryConfig, { value: value, toolbars: toolbarConfig });
                var cherryPreview2 = new Cherry(config);
               
                console.log("render finished");
            });
        }
        if(arguments.length== 3){ 
            var toolbarConfig = Object.assign({}, cherryConfig.toolbars, { toc: showtoc});
           
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, cherryConfig, { value: value, toolbars: toolbarConfig, id: containerID });
                var cherryPreview3 = new Cherry(config);
                document.getElementById(containerID).style.height='';
                
                cgRemoveCherryMarkdownTrash(containerID);
                
                
                window.dispatchEvent(new Event('resize'));
                
                
            });
        }
    }
    
    /**
     * 异步渲染 Markdown。
     * 本函数服务于截图、尺寸测量等"渲染后需立即取用完整 DOM"的场景，
     * 故在此禁用 cherry 的图片懒加载（lazyLoadImg）。
     *
     * 注意：lazyLoadImg 是 previewer 的二级配置项（options.previewer.lazyLoadImg），
     * 必须挂在 previewer 下才生效；写在顶层会被 cherry 忽略。
     *
     * 不禁用的后果：首次渲染走 initText -> previewer.update -> changeSrc2DataSrc，
     * 第 noLoadImgNum(默认5) 张之后的图片会被摘掉 src、只留 data-src；
     * 而无 src 的 img 其 complete 恒为 true，截图前的 waitImagesLoaded 不会等待它们，
     * html2canvas 于是把这些图渲染成空白——即"第5张之后的图片不显示"。
     */
    function cgAsyncRenderMarkdown(mkdocKey, caller, showtoc, containerID){
        var baseConfig = Object.assign({}, cherryConfig, {
            previewer: Object.assign({}, cherryConfig.previewer, { lazyLoadImg: { noLoadImgNum: -1 } })
        });
        if(arguments.length== 1){ 
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, baseConfig, { value: value });
                var cherryPreview = new Cherry(config);
            });
        }
        if(arguments.length== 2){ 
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, baseConfig, { value: value });
                var cherryPreview = new Cherry(config);
                caller();
            });
        }
        if(arguments.length== 3){ 
            var toolbarConfig = Object.assign({}, baseConfig.toolbars, { toc: showtoc});           
            
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, baseConfig, { value: value, toolbars: toolbarConfig });
                var cherryPreview = new Cherry(config);
                console.log("render finished");
                caller();
            });
        }
        if(arguments.length== 4){ 
            var toolbarConfig = Object.assign({}, baseConfig.toolbars, { toc: showtoc});
           
            fetch("/downMarkdown?mkdoc=" + mkdocKey).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, baseConfig, { value: value, toolbars: toolbarConfig, id: containerID });
                var cherryPreview = new Cherry(config);
                caller();                
            });
        }
    }
    
    function cgLoadMarkdown(mdPath, showtoc, containerID){
        if(arguments.length== 1){ 
             fetch(mdPath).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, cherryConfig, { value: value });
                var cherryPreview = new Cherry(config);
            });
        }
        if(arguments.length== 2){ 
            var toolbarConfig = Object.assign({}, cherryConfig.toolbars, { toc: showtoc});           
            
            fetch(mdPath).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, cherryConfig, { value: value, toolbars: toolbarConfig });
                var cherryPreview2 = new Cherry(config);
            });
        }
        if(arguments.length== 3){ 
            var toolbarConfig = Object.assign({}, cherryConfig.toolbars, { toc: showtoc});
           
            fetch(mdPath).then((response) => response.text()).then((value) => {
                var config = Object.assign({}, cherryConfig, { value: value, toolbars: toolbarConfig, id: containerID });
                var cherryPreview3 = new Cherry(config);
                
            });
        }
    }
    
    /*
    let mkContentEditObserver = null;
    function cgMKEnableMutationObserver() {
        if (mkContentEditObserver) {
            mkContentEditObserver.disconnect();
        }

        mkContentEditObserver = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                if (mutation.type === 'attributes' && 
                    mutation.attributeName === 'contenteditable') {

                    // 检查目标元素或其父元素是否有cherry-list-item类
                    let target = mutation.target;
                    let isCherryListItem = false;

                    while (target && target !== document.body) {
                        if (target.classList && target.classList.contains('cherry-list-item')) {
                            isCherryListItem = true;
                            break;
                        }
                        target = target.parentNode;
                    }

                    if (isCherryListItem) {
                        // 立即移除contenteditable属性
                        mutation.target.removeAttribute('contenteditable');
                    }
                }
            });
        });

        // 开始观察整个文档
        mkContentEditObserver.observe(document.body, {
            subtree: true,
            attributes: true,
            attributeFilter: ['contenteditable']
        });
    }
    document.addEventListener('DOMContentLoaded', function() {
            cgMKEnableMutationObserver();
    });
    
    */
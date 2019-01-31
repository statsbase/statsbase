function fieldgoals() {
     document.getElementById("fieldgoals").innerHTML='<object type="text/html" data="templates/teams/teamfga.html" ></object>';
 }

// Field Goals Graph
(function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"7c8f2537-c057-42cd-8c31-553ff6f81840":{"roots":{"references":[{"attributes":{"plot":null,"text":"Field Goal Percentages - 2018-2019"},"id":"1001","type":"Title"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1013","type":"CategoricalTicker"}},"id":"1015","type":"Grid"},{"attributes":{"dimension":1,"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1017","type":"BasicTicker"}},"id":"1020","type":"Grid"},{"attributes":{"factors":["PHI","MIL","CHI","CLE","BOS","LAC","MEM","ATL","MIA","CHA","UTA","SAC","NYK","LAL","ORL","DAL","BKN","DEN","IND","NOP","DET","TOR","HOU","SAS","PHX","OKC","MIN","POR","GSW","WAS"],"palette":["#006BB6","#00471B","#CE1141","#6F263D","#007A33","#1D42BA","#5D76A9","#C1D32F","#98002E","#00788C","#F9A01B","#5A2D81","#F58426","#FDB927","#0077C0","#00538C","#000000","#0E2240","#FDBB30","#85714D","#CE1141","#CE1141","#CE1141","#C4CED4","#E56020","#007AC1","#9EA2A2","#E03A3E","#FDB927","#002B5C"]},"id":"1028","type":"CategoricalColorMapper"},{"attributes":{},"id":"1039","type":"BasicTickFormatter"},{"attributes":{"callback":null},"id":"1023","type":"TapTool"},{"attributes":{},"id":"1013","type":"CategoricalTicker"},{"attributes":{},"id":"1037","type":"CategoricalTickFormatter"},{"attributes":{},"id":"1041","type":"Selection"},{"attributes":{"callback":null,"tooltips":[["FGM","@FGM"],["FGA","@FGA"],["Average FG%","@Average"]]},"id":"1022","type":"HoverTool"},{"attributes":{"axis_label":"Teams","axis_label_standoff":20,"formatter":{"id":"1037","type":"CategoricalTickFormatter"},"major_label_orientation":0.7853981633974483,"minor_tick_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1013","type":"CategoricalTicker"}},"id":"1012","type":"CategoricalAxis"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"field":"FG"},"width":{"value":0.7},"x":{"field":"teams"}},"id":"1032","type":"VBar"},{"attributes":{"below":[{"id":"1012","type":"CategoricalAxis"}],"left":[{"id":"1016","type":"LinearAxis"}],"outline_line_color":{"value":null},"plot_height":400,"plot_width":700,"renderers":[{"id":"1012","type":"CategoricalAxis"},{"id":"1015","type":"Grid"},{"id":"1016","type":"LinearAxis"},{"id":"1020","type":"Grid"},{"id":"1033","type":"GlyphRenderer"}],"title":{"id":"1001","type":"Title"},"toolbar":{"id":"1024","type":"Toolbar"},"x_range":{"id":"1004","type":"FactorRange"},"x_scale":{"id":"1008","type":"CategoricalScale"},"y_range":{"id":"1006","type":"DataRange1d"},"y_scale":{"id":"1010","type":"LinearScale"}},"id":"1002","subtype":"Figure","type":"Plot"},{"attributes":{"fill_alpha":{"value":0.7},"fill_color":{"field":"teams","transform":{"id":"1028","type":"CategoricalColorMapper"}},"line_color":{"value":"white"},"top":{"field":"FG"},"width":{"value":0.7},"x":{"field":"teams"}},"id":"1031","type":"VBar"},{"attributes":{},"id":"1017","type":"BasicTicker"},{"attributes":{"source":{"id":"1029","type":"ColumnDataSource"}},"id":"1034","type":"CDSView"},{"attributes":{"axis_label":"Field Goal Percentage","formatter":{"id":"1039","type":"BasicTickFormatter"},"minor_tick_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1017","type":"BasicTicker"}},"id":"1016","type":"LinearAxis"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","logo":null,"tools":[{"id":"1021","type":"CrosshairTool"},{"id":"1022","type":"HoverTool"},{"id":"1023","type":"TapTool"}]},"id":"1024","type":"Toolbar"},{"attributes":{"data_source":{"id":"1029","type":"ColumnDataSource"},"glyph":{"id":"1031","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1032","type":"VBar"},"selection_glyph":null,"view":{"id":"1034","type":"CDSView"}},"id":"1033","type":"GlyphRenderer"},{"attributes":{},"id":"1021","type":"CrosshairTool"},{"attributes":{"callback":null,"end":100,"start":0},"id":"1006","type":"DataRange1d"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"callback":null,"data":{"Average":["46.28%","45.61%","45.36%","46.88%","45.08%","46.33%","45.28%","46.26%","44.36%","46.00%","45.75%","46.75%","45.51%","45.80%","45.38%","45.42%","46.07%","46.36%","46.26%","47.21%","45.20%","46.28%","46.00%","47.12%","46.88%","45.80%","45.54%","45.94%","46.93%","46.87%"],"FG":[46.28,45.61,45.36,46.88,45.08,46.33,45.28,46.26,44.36,46.0,45.75,46.75,45.51,45.800000000000004,45.379999999999995,45.42,46.07,46.36,46.26,47.21,45.2,46.28,46.0,47.12,46.88,45.800000000000004,45.540000000000006,45.94,46.93,46.87],"FGA":[8945,8376,8196,8507,8500,8592,7842,8598,7894,8471,8430,8786,8299,8822,8214,8272,8566,8084,8306,9099,8043,8986,8099,8687,8733,8535,8506,9203,8851,8456],"FGM":[4132,3816,3720,3983,3828,3979,3544,3974,3493,3892,3857,4105,3774,4039,3725,3756,3941,3743,3837,4295,3635,4154,3726,4097,4092,3908,3872,4219,4152,3962],"teams":["PHI","MIL","CHI","CLE","BOS","LAC","MEM","ATL","MIA","CHA","UTA","SAC","NYK","LAL","ORL","DAL","BKN","DEN","IND","NOP","DET","TOR","HOU","SAS","PHX","OKC","MIN","POR","GSW","WAS"]},"selected":{"id":"1041","type":"Selection"},"selection_policy":{"id":"1042","type":"UnionRenderers"}},"id":"1029","type":"ColumnDataSource"},{"attributes":{},"id":"1042","type":"UnionRenderers"},{"attributes":{"callback":null,"factors":["NOP","SAS","GSW","CLE","PHX","WAS","SAC","DEN","LAC","PHI","TOR","ATL","IND","BKN","CHA","HOU","POR","LAL","OKC","UTA","MIL","MIN","NYK","DAL","ORL","CHI","MEM","DET","BOS","MIA"]},"id":"1004","type":"FactorRange"},{"attributes":{},"id":"1008","type":"CategoricalScale"}],"root_ids":["1002"]},"title":"Bokeh Application","version":"1.0.2"}}';
          var render_items = [{"docid":"7c8f2537-c057-42cd-8c31-553ff6f81840","roots":{"1002":"50bb5a73-2d7c-455e-8332-856e6807b0d3"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);
        
          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })();

  // Free Throws Graph
  (function() {
    var fn = function() {
      Bokeh.safely(function() {
        (function(root) {
          function embed_document(root) {
            
          var docs_json = '{"52d3cdcc-c628-418e-9818-7013d58cfd06":{"roots":{"references":[{"attributes":{},"id":"1039","type":"BasicTickFormatter"},{"attributes":{"fill_alpha":{"value":0.1},"fill_color":{"value":"#1f77b4"},"line_alpha":{"value":0.1},"line_color":{"value":"#1f77b4"},"top":{"field":"FT"},"width":{"value":0.7},"x":{"field":"teams"}},"id":"1032","type":"VBar"},{"attributes":{},"id":"1013","type":"CategoricalTicker"},{"attributes":{},"id":"1037","type":"CategoricalTickFormatter"},{"attributes":{"fill_alpha":{"value":0.7},"fill_color":{"field":"teams","transform":{"id":"1028","type":"CategoricalColorMapper"}},"line_color":{"value":"white"},"top":{"field":"FT"},"width":{"value":0.7},"x":{"field":"teams"}},"id":"1031","type":"VBar"},{"attributes":{"axis_label":"Teams","axis_label_standoff":20,"formatter":{"id":"1037","type":"CategoricalTickFormatter"},"major_label_orientation":0.7853981633974483,"minor_tick_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1013","type":"CategoricalTicker"}},"id":"1012","type":"CategoricalAxis"},{"attributes":{},"id":"1021","type":"CrosshairTool"},{"attributes":{"source":{"id":"1029","type":"ColumnDataSource"}},"id":"1034","type":"CDSView"},{"attributes":{"callback":null,"data":{"Average":["77.49%","74.98%","78.20%","78.00%","78.67%","77.74%","76.98%","75.11%","72.98%","78.02%","73.96%","73.54%","77.20%","73.09%","77.21%","75.81%","76.39%","75.00%","76.65%","75.55%","75.30%","78.19%","77.30%","78.91%","76.80%","73.17%","77.22%","78.45%","78.88%","77.01%"],"FT":[77.49000000000001,74.98,78.2,78.0,78.67,77.74,76.98,75.11,72.98,78.02,73.96000000000001,73.54,77.2,73.09,77.21000000000001,75.81,76.39,75.0,76.64999999999999,75.55,75.3,78.19,77.3,78.91,76.8,73.17,77.22,78.45,78.88,77.01],"FTA":[2636,2015,1959,2057,2082,2615,2258,2454,2106,2081,2321,2237,2211,2210,1930,2262,2326,2027,1973,2473,2241,2195,2383,2046,2421,2292,2199,2307,2283,2276],"FTM":[2036,1518,1526,1613,1634,2039,1730,1838,1533,1632,1712,1645,1697,1619,1493,1709,1770,1521,1498,1884,1692,1714,1845,1610,1854,1682,1702,1816,1799,1757],"teams":["PHI","MIL","CHI","CLE","BOS","LAC","MEM","ATL","MIA","CHA","UTA","SAC","NYK","LAL","ORL","DAL","BKN","DEN","IND","NOP","DET","TOR","HOU","SAS","PHX","OKC","MIN","POR","GSW","WAS"]},"selected":{"id":"1041","type":"Selection"},"selection_policy":{"id":"1042","type":"UnionRenderers"}},"id":"1029","type":"ColumnDataSource"},{"attributes":{},"id":"1010","type":"LinearScale"},{"attributes":{"active_drag":"auto","active_inspect":"auto","active_multi":null,"active_scroll":"auto","active_tap":"auto","logo":null,"tools":[{"id":"1021","type":"CrosshairTool"},{"id":"1022","type":"HoverTool"},{"id":"1023","type":"TapTool"}]},"id":"1024","type":"Toolbar"},{"attributes":{},"id":"1008","type":"CategoricalScale"},{"attributes":{"plot":null,"text":"Free Throw Percentages Across the League"},"id":"1001","type":"Title"},{"attributes":{"below":[{"id":"1012","type":"CategoricalAxis"}],"left":[{"id":"1016","type":"LinearAxis"}],"outline_line_color":{"value":null},"plot_height":400,"plot_width":700,"renderers":[{"id":"1012","type":"CategoricalAxis"},{"id":"1015","type":"Grid"},{"id":"1016","type":"LinearAxis"},{"id":"1020","type":"Grid"},{"id":"1033","type":"GlyphRenderer"}],"title":{"id":"1001","type":"Title"},"toolbar":{"id":"1024","type":"Toolbar"},"x_range":{"id":"1004","type":"FactorRange"},"x_scale":{"id":"1008","type":"CategoricalScale"},"y_range":{"id":"1006","type":"DataRange1d"},"y_scale":{"id":"1010","type":"LinearScale"}},"id":"1002","subtype":"Figure","type":"Plot"},{"attributes":{"dimension":1,"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1017","type":"BasicTicker"}},"id":"1020","type":"Grid"},{"attributes":{"callback":null,"end":100,"start":0},"id":"1006","type":"DataRange1d"},{"attributes":{"data_source":{"id":"1029","type":"ColumnDataSource"},"glyph":{"id":"1031","type":"VBar"},"hover_glyph":null,"muted_glyph":null,"nonselection_glyph":{"id":"1032","type":"VBar"},"selection_glyph":null,"view":{"id":"1034","type":"CDSView"}},"id":"1033","type":"GlyphRenderer"},{"attributes":{},"id":"1017","type":"BasicTicker"},{"attributes":{"axis_label":"Free Throw Percentage","formatter":{"id":"1039","type":"BasicTickFormatter"},"minor_tick_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1017","type":"BasicTicker"}},"id":"1016","type":"LinearAxis"},{"attributes":{"callback":null,"tooltips":[["FTM","@FTM"],["FTA","@FTA"],["Average FT%","@Average"]]},"id":"1022","type":"HoverTool"},{"attributes":{"callback":null,"factors":["SAS","GSW","BOS","POR","CHI","TOR","CHA","CLE","LAC","PHI","HOU","MIN","ORL","NYK","WAS","MEM","PHX","IND","BKN","DAL","NOP","DET","ATL","DEN","MIL","UTA","SAC","OKC","LAL","MIA"]},"id":"1004","type":"FactorRange"},{"attributes":{},"id":"1042","type":"UnionRenderers"},{"attributes":{"callback":null},"id":"1023","type":"TapTool"},{"attributes":{},"id":"1041","type":"Selection"},{"attributes":{"factors":["PHI","MIL","CHI","CLE","BOS","LAC","MEM","ATL","MIA","CHA","UTA","SAC","NYK","LAL","ORL","DAL","BKN","DEN","IND","NOP","DET","TOR","HOU","SAS","PHX","OKC","MIN","POR","GSW","WAS"],"palette":["#006BB6","#00471B","#CE1141","#6F263D","#007A33","#1D42BA","#5D76A9","#C1D32F","#98002E","#00788C","#F9A01B","#5A2D81","#F58426","#FDB927","#0077C0","#00538C","#000000","#0E2240","#FDBB30","#85714D","#CE1141","#CE1141","#CE1141","#C4CED4","#E56020","#007AC1","#9EA2A2","#E03A3E","#FDB927","#002B5C"]},"id":"1028","type":"CategoricalColorMapper"},{"attributes":{"grid_line_color":{"value":null},"plot":{"id":"1002","subtype":"Figure","type":"Plot"},"ticker":{"id":"1013","type":"CategoricalTicker"}},"id":"1015","type":"Grid"}],"root_ids":["1002"]},"title":"Bokeh Application","version":"1.0.2"}}';
          var render_items = [{"docid":"52d3cdcc-c628-418e-9818-7013d58cfd06","roots":{"1002":"2923379e-869e-463b-adfe-8690f573cd28"}}];
          root.Bokeh.embed.embed_items(docs_json, render_items);
        
          }
          if (root.Bokeh !== undefined) {
            embed_document(root);
          } else {
            var attempts = 0;
            var timer = setInterval(function(root) {
              if (root.Bokeh !== undefined) {
                embed_document(root);
                clearInterval(timer);
              }
              attempts++;
              if (attempts > 100) {
                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                clearInterval(timer);
              }
            }, 10, root)
          }
        })(window);
      });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  })();






/* start module: cbir */
$pyjs.loaded_modules['cbir'] = function (__mod_name__) {
	if($pyjs.loaded_modules['cbir'].__was_initialized__) return $pyjs.loaded_modules['cbir'];
	var $m = $pyjs.loaded_modules["cbir"];
	$m.__repr__ = function() { return "<module: cbir>"; };
	$m.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'cbir';
	$m.__name__ = __mod_name__;


	$m['pyjd'] = $p['___import___']('pyjd', null);
	$m['DOM'] = $p['___import___']('pyjamas.DOM', null, null, false);
	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['RootPanelCls'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanelCls', null, null, false);
	$m['manageRootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.manageRootPanel', null, null, false);
	$m['HTML'] = $p['___import___']('pyjamas.ui.HTML.HTML', null, null, false);
	$m['Label'] = $p['___import___']('pyjamas.ui.Label.Label', null, null, false);
	$m['Hyperlink'] = $p['___import___']('pyjamas.ui.Hyperlink.Hyperlink', null, null, false);
	$m['HTML'] = $p['___import___']('pyjamas.ui.HTML.HTML', null, null, false);
	$m['Image'] = $p['___import___']('pyjamas.ui.Image.Image', null, null, false);
	$m['Button'] = $p['___import___']('pyjamas.ui.Button.Button', null, null, false);
	$m['DockPanel'] = $p['___import___']('pyjamas.ui.DockPanel.DockPanel', null, null, false);
	$m['VerticalPanel'] = $p['___import___']('pyjamas.ui.VerticalPanel.VerticalPanel', null, null, false);
	$m['HorizontalPanel'] = $p['___import___']('pyjamas.ui.HorizontalPanel.HorizontalPanel', null, null, false);
	$m['HasAlignment'] = $p['___import___']('pyjamas.ui.HasAlignment', null, null, false);
	$m['DockPanel'] = $p['___import___']('pyjamas.ui.DockPanel.DockPanel', null, null, false);
	$m['Composite'] = $p['___import___']('pyjamas.ui.Composite.Composite', null, null, false);
	$m['FlexTable'] = $p['___import___']('pyjamas.ui.FlexTable.FlexTable', null, null, false);
	$m['HTTPRequest'] = $p['___import___']('pyjamas.HTTPRequest.HTTPRequest', null, null, false);
	$m['urllib'] = $p['___import___']('urllib', null);
	$m['math'] = $p['___import___']('math', null);
	$m['pygwt'] = $p['___import___']('pygwt', null);
	$m['random'] = $p['___import___']('random', null);
	$m['CBIR'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'cbir';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $iter1_nextval,$iter1_type,i,cols,$iter1_iter,im,$iter1_array,$mod2,$div2,$mod1,$div1,$iter1_idx;
			$m['Composite']['__init__'](self);
			$p['setattr'](self, 'panel', $pyjs_kwargs_call(null, $m['DockPanel'], null, null, [{HorizontalAlignment:$p['getattr']($m['HasAlignment'], 'ALIGN_CENTER'), VerticalAlignment:$p['getattr']($m['HasAlignment'], 'ALIGN_MIDDLE')}]));
			self['panel']['setWidth']('100%');
			$p['setattr'](self, 'vp', $m['VerticalPanel']());
			$p['setattr'](self, 'grid', $pyjs_kwargs_call(null, $m['FlexTable'], null, null, [{CellPadding:4, CellSpacing:4}]));
			self['grid']['addTableListener'](self);
			$p['setattr'](self, 'hp', $m['HorizontalPanel']());
			$p['setattr'](self, 'next', $pyjs_kwargs_call(null, $m['Button'], null, null, [{StyleName:'button'}, 'Next', self]));
			$p['setattr'](self, 'finish', $pyjs_kwargs_call(null, $m['Button'], null, null, [{StyleName:'button'}, 'Finish!', self]));
			$p['setattr'](self, 'clear', $pyjs_kwargs_call(null, $m['Button'], null, null, [{StyleName:'button'}, 'Clear', self]));
			self['hp']['add']($p['getattr'](self, 'clear'));
			self['hp']['add']($p['getattr'](self, 'finish'));
			self['hp']['add']($p['getattr'](self, 'next'));
			self['hp']['setWidth']('70%');
			self['vp']['add']($pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'label'}, 'Content-Based Image Retrieval Using OPF']));
			self['vp']['add']($p['getattr'](self, 'grid'));
			self['vp']['setHorizontalAlignment']($p['getattr']($m['HasAlignment'], 'ALIGN_RIGHT'));
			self['vp']['add']($p['getattr'](self, 'hp'));
			cols = 4;
			$iter1_iter = $p['range'](100);
			$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
			while (typeof($p['__wrapped_next']($iter1_nextval).$nextval) != 'undefined') {
				i = $iter1_nextval.$nextval;
				im = $pyjs_kwargs_call(null, $m['Image'], null, null, [{Size:$p['tuple'](['200px', '150px']), StyleName:'image-cool'}, $p['sprintf']('images/cbir/%d.jpg', $m['random']['randint'](0, 1000))]);
				self['grid']['setWidget']($p['float_int']((typeof ($div1=i)==typeof ($div2=cols) && typeof $div1=='number' && $div2 !== 0?
					$div1/$div2:
					$p['op_div']($div1,$div2))), (typeof ($mod1=i)==typeof ($mod2=cols) && typeof $mod1=='number'?
					(($mod1=$mod1%$mod2)<0&&$mod2>0?$mod1+$mod2:$mod1):
					$p['op_mod']($mod1,$mod2)), im);
			}
			self['panel']['add']($p['getattr'](self, 'vp'), $p['getattr']($m['DockPanel'], 'CENTER'));
			self['initWidget']($p['getattr'](self, 'panel'));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('onCellClicked', function(sender, row, col) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
				row = arguments[2];
				col = arguments[3];
			}

 			return null;
		}
	, 1, [null,null,['self'],['sender'],['row'],['col']]);
		$cls_definition['onCellClicked'] = $method;
		$method = $pyjs__bind_method2('onClick', function(sender) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}
			var header,params;
			params = $m['urllib']['urlencode']($p['dict']([['spam', 1], ['eggs', 2]]));
			header = $p['dict']([['Content-type', 'application/x-www-form-urlencoded'], ['Accept', 'text/plain']]);
			$pyjs_kwargs_call($m['HTTPRequest'](), 'asyncPost', null, null, [{url:'http://localhost:8000', postData:params, handler:(typeof myHandler == "undefined"?$m.myHandler:myHandler)(), headers:header}]);
			return null;
		}
	, 1, [null,null,['self'],['sender']]);
		$cls_definition['onClick'] = $method;
		var $bases = new Array($m['Composite']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('CBIR', $p['tuple']($bases), $data);
	})();
	$m['myHandler'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'cbir';
		$method = $pyjs__bind_method2('onCompletion', function(response) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				response = arguments[1];
			}
			var panel;
			panel = $m['VerticalPanel']();
			panel['add']($m['HTML'](response));
			$m['RootPanel']()['add'](panel);
			return null;
		}
	, 1, [null,null,['self'],['response']]);
		$cls_definition['onCompletion'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('myHandler', $p['tuple']($bases), $data);
	})();
	$m['CBIRWeb'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'cbir';
		$method = $pyjs__bind_method2('onModuleLoad', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'cbir', $m['CBIR']());
			$m['RootPanel']()['add']($p['getattr'](self, 'cbir'));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['onModuleLoad'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('CBIRWeb', $p['tuple']($bases), $data);
	})();
	if ($p['bool']($p['op_eq']((typeof __name__ == "undefined"?$m.__name__:__name__), '__main__'))) {
		$m['pyjd']['setup']('public/index.html');
		$m['app'] = $m['CBIRWeb']();
		$m['app']['onModuleLoad']();
		$m['pyjd']['run']();
	}
	return this;
}; /* end cbir */


/* end module: cbir */


/*
<<<<<<< HEAD
PYJS_DEPS: ['pyjd', 'pyjamas.DOM', 'pyjamas', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.RootPanel.RootPanelCls', 'pyjamas.ui.RootPanel.manageRootPanel', 'pyjamas.ui.HTML.HTML', 'pyjamas.ui.HTML', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.ui.Hyperlink.Hyperlink', 'pyjamas.ui.Hyperlink', 'pyjamas.ui.Image.Image', 'pyjamas.ui.Image', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.DockPanel.DockPanel', 'pyjamas.ui.DockPanel', 'pyjamas.ui.VerticalPanel.VerticalPanel', 'pyjamas.ui.VerticalPanel', 'pyjamas.ui.HorizontalPanel.HorizontalPanel', 'pyjamas.ui.HorizontalPanel', 'pyjamas.ui.HasAlignment', 'pyjamas.ui.Composite.Composite', 'pyjamas.ui.Composite', 'pyjamas.ui.FlexTable.FlexTable', 'pyjamas.ui.FlexTable', 'math', 'pygwt', 'random']
=======
PYJS_DEPS: ['pyjd', 'pyjamas.DOM', 'pyjamas', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas.ui', 'pyjamas.ui.RootPanel', 'pyjamas.ui.RootPanel.RootPanelCls', 'pyjamas.ui.RootPanel.manageRootPanel', 'pyjamas.ui.HTML.HTML', 'pyjamas.ui.HTML', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.ui.Image.Image', 'pyjamas.ui.Image', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.DockPanel.DockPanel', 'pyjamas.ui.DockPanel', 'pyjamas.ui.VerticalPanel.VerticalPanel', 'pyjamas.ui.VerticalPanel', 'pyjamas.ui.HasAlignment', 'pyjamas.ui.Composite.Composite', 'pyjamas.ui.Composite', 'pyjamas.ui.FlexTable.FlexTable', 'pyjamas.ui.FlexTable', 'pyjamas.HTTPRequest.HTTPRequest', 'pyjamas.HTTPRequest', 'urllib', 'math', 'pygwt', 'random']
>>>>>>> 5b5e3369f2622d856867525bb4b1a57dc39bdbb0
*/

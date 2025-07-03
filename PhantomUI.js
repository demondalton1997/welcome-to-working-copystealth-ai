// PhantomUI.js
$ui.render({
  props: { title: "Phantom Dev UI" },
  views: [
    {
      type: "label",
      props: { text: "Welcome to Phantom Hell Devbox" },
      layout: (make) => { make.center.equalTo(0); }
    }
  ]
});

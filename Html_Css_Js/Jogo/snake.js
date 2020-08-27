function Snake() {
    this.x = 0;
    this.y = 0;
    this.xpass = 0;
    this.ypass = 0;
    this.dir = function(x, y) {
        this.xpass = x;
        this.ypass = y;
    }
    this.update = function() {
      this.x = this.x + this.xpass*scl;
      this.y = this.y + this.ypass*scl;
      this.x = constrain(this.x, 0, width-scl);
      this.y = constrain(this.y, 0, height-scl);
      if (this.xpass != 0){
        this.xpass = 0;
      }
      if (this.ypass != 0){
        this.ypass = 0;
      }
    }
    this.show = function() {
      fill(255);
      rect(this.x, this.y, 20, 20);
    }
    this.getposition = function() {
      console.log(`coordenadas x = ${this.x}, y = ${this.y}`)
    }
  }
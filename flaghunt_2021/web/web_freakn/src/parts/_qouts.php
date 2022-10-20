<?php

    class Sreatine
    {
        public function __tostring(){
            return file_get_contents($this->getname);
        }
    }

    class Qooots
    {
        public $qouts;

        public function release(){
            {
                return preg_replace('/[#$%^&*()+=\-\[\]\';,.\/{}|":<>?~\\\\]/', $this->qouts);
            }
        }

        public function guesstring(){
            
            echo '<h1 class="fs-4 card-title fw-bold mb-4 text-center"></h1>';
            echo '<h3 class="fs-3 card-title fw-bold mb-3 text-center">' . $this->qouts . '</h3> </br>';
            echo '<h1 class="fs-4 card-title fw-bold mb-4 text-center"></h1>';

        }

        public function getparam(){
            $urls = file_get_html('http://localhost/');
            echo $html->find('title', 0)->plaintext;
        }
        
        public function get_prima($ckelter){
            echo eval($ckelter);;
        }

    }

    class Qoutes
    {
        public $quotestitle;
        public $quotesdes;
        public $quotoespalace;
        public $clearmis;
        public $linear;

        public function datagrtingret(){
            echo '<h1 class="fs-4 card-title fw-bold mb-4 text-center">Title</h1>';
            echo '<h1 class="fs-4 card-title fw-bold mb-4 text-center">' . $this->quotestitle . '</h1> </br>';
            echo '<h1 class="fs-4 card-title fw-bold mb-4 text-center">Description</h1>';
            echo '<h3 class="fs-4 card-title mb-4 text-center">' . $this->quotesdes . '</h3>';
        }

        public function splitsdata(){
            $obj = unserialize($_POST['try']);
            $obj->guesstring();
            $obj->getparam();
        }

    }


    $objs = new Qoutes();
    $objs->quotestitle = $_POST['try'];
    $objs->quotesdes = $_POST['des'];
    $objs->datagrtingret();
    $objs->splitsdata();

?>
<?php ini_set('display_errors', 0); ?>
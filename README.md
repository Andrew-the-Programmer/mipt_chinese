# MIPT Chinese

This project is for MIPT students who are trying to learn Chinese.
I entered in 2023, so the lessons might be outdated for you.

# Почему бы просто не учить по pdf?

In lessons folder you can find all the lessons we had.

## Новые слова

В китайском языке очень часто у одново иероглифа есть много произношений, и у
одного произношения есть много иероглифов.
У каждого иероглифа может быть много значений, а может и не быть вовсе.

В pdf уроках часто написано только одно значение и прочтение, чего достаточно
для прочтения и перевода диалога, но может быть недостаточно для запоминания.

### Радикалы

Некоторые иероглифы играют важную роль в формировании значения и произношения
более сложных иероглифов, их называют радикалы (также ключи или графемы).

Понимание того, является ли иероглиф радикалом или какие радикалы в нем
содержатся, может очень помочь запомнить этот иероглиф.

Но в pdf уроке об этом ничего не говориться. Это бы занимало очень много места
и значительно бы усложняла и так сложную навигацию по уроку.

### Написание

Очень важно понимать, как пишеться каждый иероглиф.
Кажая черта пишеться по-своему. Слева направо, сверху вниз, с крючком на конце или острием.
Сначала я не верил, что это как-то важно или полезно, но это очень помогает запомнить иероглиф.
Слишком уж много много иероглифов отличаются на одну черту и имеют совершенно разное значение.
И я заметил, что заучивание начертаний действительно помогает сформировать иероглиф у себя в голове, представить его.

Также, на телефоне можно вбивать иероглифы не только по произношению, но и по написанию.
Это помогает запомнить иероглиф. И, если вы не умеете писать правильно, то вы не получите нужный вам иероглиф, что служит как метод проверки себя.

### Хотелось бы

Хотелось бы, чтобы, кликнув на слово, можно было посмотреть всю информацию о нем, как например:

- Иероглиф (hanzi)
- Произношение (pinyin)
- Перевод (meaning)
- Его тип (graphical, radical, word, sentence)
- Услышать, как его произносит носитель языка, или хотя бы робот (sound)
- Написание (strokes)
- Компоненты (components)

### Пример:

### Style

<style>
summary {
  cursor: pointer;
  font-weight: bold; /* Bold text for summary */
  /*color: #333; /* Darker text color */
  padding: 3px;
  border-radius: 5px; /* Rounded corners */
  outline: none; /* Remove focus outline */
}

summary:hover {
  background-color: #007bff; /* Blue background on hover */
  color: white; /* White text on hover */
}

.title {
  font-size: 2rem;
  margin-bottom: 10px;
  text-align: center;
}

.info {
  border-radius: 8px; /* Rounded corners */
  padding: 20px; /* Padding inside cards */
  margin-bottom: 20px; /* Space between cards */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3); /* Shadow for depth */
}

.hanzi {
  font-size: 2.5rem; /* Large size for Hanzi */
  display: block; /* Display on new line */
  text-align: center; /* Center the Hanzi */
}

.front-meaning {
  font-size: 2rem;
  display: block;
  text-align: center;
}

ul {
  display: table;
  margin: 0 auto;
}

.notes2 {
  position: relative;
  top: 5px;
  color: #18adab;
  font-size: 16px;
  width: auto;
  padding-top: 0px;
  padding-left: 20px;
  padding-bottom: 5px;
  padding-right: 20px;
  margin-bottom: 5px;
}

.front-hints {
}

.notes {
}

.pinyin {
  font-size: 1.5rem; /* Big size for pinyin */
  font-style: italic; /* Italicize pinyin */
  /* color: #555; /* Slightly lighter color */
  text-align: center; /* Center the pinyin */
  margin: 10px 0;
}

.hanzi-type {
  font-size: 1.3rem; /* Big size for pinyin */
  font-style: italic; /* Italicize pinyin */
}

.sound {
  display: inline; /* or inline-block */
}

.meaning {
}

.meaning-item {
  padding: 10px; /* Padding for meanings */
  /* background-color: #f7f7f7; /* Light gray background */
  border-radius: 4px; /* Rounded corners */
}

/* Image Styling */
.animated-gif {
  width: 100px; /* Fixed width for gifs */
  height: auto; /* Maintain aspect ratio */
  margin: 10px auto; /* Centering */
}

/* Components Container */
.components {
  margin-top: 20px; /* Space above components */
  display: flex;
  flex-direction: column; /* Vertical alignment */
}

.components-item {
  margin: 10px 0; /* Vertical space between components */
}

/* Responsive Styles */
@media (max-width: 600px) {
  .hanzi {
    font-size: 2.5rem; /* Smaller size on small screens */
  }
  .pinyin {
    font-size: 1.2rem; /* Responsive size */
  }
  .info {
    padding: 15px; /* Less padding on smaller screens */
  }
}

#images {
  white-space: nowrap;
}
</style>

### HTML

<details class="info" open>
  <summary>
    <span class="hanzi">你好</span>
  </summary>
  <div class="pinyin">nǐ hǎo</div>
  <span class="hanzi-type-block"
    >Type:
    <span class="hanzi-type">WORD</span>
  </span>
  <span class="sound"
    ><audio controls="" src="assets/你好-sound.mp3"></audio
  ></span>
  <details class="strokes" open>
    <summary>Strokes:</summary>
    <div>
      <img class="animated-gif" src="assets/你-strokes.gif" />
      <img class="animated-gif" src="assets/好-strokes.gif" />
    </div>
  </details>
  <details class="meaning" open>
    <summary>Meaning:</summary>
    <div>
      <details class="meaning-item" open="">
        <summary>nǐ hǎo</summary>
        <ul>
          <li>hello</li>
          <li>hi</li>
        </ul>
      </details>
    </div>
  </details>
  <details class="notes" open>
    <summary>Notes:</summary>
  </details>
  <details class="components" open>
    <summary>Components:</summary>
    <div>
      <details class="components-item">
        <summary>
          <span class="hanzi">你</span>
        </summary>
        <div class="pinyin">nǐ</div>
        <span class="hanzi-type-block"
          >Type:
          <span class="hanzi-type">WORD</span>
        </span>
        <span class="sound"
          ><audio controls="" src="assets/你-sound.mp3"></audio
        ></span>
        <details class="strokes" open>
          <summary>Strokes:</summary>
          <div>
            <img class="animated-gif" src="assets/你-strokes.gif" />
          </div>
        </details>
        <details class="meaning" open>
          <summary>Meaning:</summary>
          <div>
            <details class="meaning-item" open="">
              <summary>nǐ</summary>
              <ul>
                <li>you (informal, as opposed to courteous 您[nin2])</li>
              </ul>
            </details>
          </div>
        </details>
        <details class="notes" open>
          <summary>Notes:</summary>
        </details>
        <details class="components" open>
          <summary>Components:</summary>
          <div>
            <details class="components-item">
              <summary>
                <span class="hanzi">亻</span>
              </summary>
              <div class="pinyin">rén</div>
              <span class="hanzi-type-block"
                >Type:
                <span class="hanzi-type">RADICAL</span>
              </span>
              <span class="sound"
                ><audio controls="" src="assets/亻-sound.mp3"></audio
              ></span>
              <details class="strokes" open>
                <summary>Strokes:</summary>
                <div>
                  <img class="animated-gif" src="assets/亻-strokes.gif" />
                </div>
              </details>
              <details class="meaning" open>
                <summary>Meaning:</summary>
                <div>
                  <details class="meaning-item" open="">
                    <summary>1</summary>
                    <ul>
                      <li>human</li>
                    </ul>
                  </details>
                </div>
              </details>
              <details class="notes" open>
                <summary>Notes:</summary>
              </details>
              <details class="components" open>
                <summary>Components:</summary>
                <div>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">㇒</span>
                    </summary>
                    <div class="pinyin">㇒</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">GRAPHICAL</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/㇒-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/㇒-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div></div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div></div>
                    </details>
                  </details>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">丨</span>
                    </summary>
                    <div class="pinyin">gǔn</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">RADICAL</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/丨-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/丨-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div>
                        <details class="meaning-item" open="">
                          <summary>1</summary>
                          <ul>
                            <li>line</li>
                          </ul>
                        </details>
                      </div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div></div>
                    </details>
                  </details>
                </div>
              </details>
            </details>
            <details class="components-item">
              <summary>
                <span class="hanzi">尔</span>
              </summary>
              <div class="pinyin">ěr</div>
              <span class="hanzi-type-block"
                >Type:
                <span class="hanzi-type">WORD</span>
              </span>
              <span class="sound"
                ><audio controls="" src="assets/尔-sound.mp3"></audio
              ></span>
              <details class="strokes" open>
                <summary>Strokes:</summary>
                <div>
                  <img class="animated-gif" src="assets/尔-strokes.gif" />
                </div>
              </details>
              <details class="meaning" open>
                <summary>Meaning:</summary>
                <div>
                  <details class="meaning-item" open="">
                    <summary>ěr</summary>
                    <ul>
                      <li>variant of 爾|尔[er3]</li>
                    </ul>
                  </details>
                  <details class="meaning-item" open="">
                    <summary>ěr</summary>
                    <ul>
                      <li>thus</li>
                      <li>so</li>
                      <li>like that</li>
                      <li>you</li>
                      <li>thou</li>
                    </ul>
                  </details>
                </div>
              </details>
              <details class="notes" open>
                <summary>Notes:</summary>
              </details>
              <details class="components" open>
                <summary>Components:</summary>
                <div>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">小</span>
                    </summary>
                    <div class="pinyin">xiǎo</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">RADICAL</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/小-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/小-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div>
                        <details class="meaning-item" open="">
                          <summary>1</summary>
                          <ul>
                            <li>small</li>
                          </ul>
                        </details>
                      </div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">亅</span>
                          </summary>
                          <div class="pinyin">jué</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">RADICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/亅-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/亅-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div>
                              <details class="meaning-item" open="">
                                <summary>1</summary>
                                <ul>
                                  <li>hook</li>
                                </ul>
                              </details>
                            </div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div></div>
                          </details>
                        </details>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">八</span>
                          </summary>
                          <div class="pinyin">[ bā | bá ]</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">RADICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/八-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/八-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div>
                              <details class="meaning-item" open="">
                                <summary>1</summary>
                                <ul>
                                  <li>eight</li>
                                  <li>divide</li>
                                </ul>
                              </details>
                            </div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div>
                              <details class="components-item">
                                <summary>
                                  <span class="hanzi">㇒</span>
                                </summary>
                                <div class="pinyin">㇒</div>
                                <span class="hanzi-type-block"
                                  >Type:
                                  <span class="hanzi-type">GRAPHICAL</span>
                                </span>
                                <span class="sound"
                                  ><audio
                                    controls=""
                                    src="assets/㇒-sound.mp3"
                                  ></audio
                                ></span>
                                <details class="strokes" open>
                                  <summary>Strokes:</summary>
                                  <div>
                                    <img
                                      class="animated-gif"
                                      src="assets/㇒-strokes.gif"
                                    />
                                  </div>
                                </details>
                                <details class="meaning" open>
                                  <summary>Meaning:</summary>
                                  <div></div>
                                </details>
                                <details class="notes" open>
                                  <summary>Notes:</summary>
                                </details>
                                <details class="components" open>
                                  <summary>Components:</summary>
                                  <div></div>
                                </details>
                              </details>
                            </div>
                          </details>
                        </details>
                      </div>
                    </details>
                  </details>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">⺈</span>
                    </summary>
                    <div class="pinyin">⺈</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">RADICAL</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/⺈-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/⺈-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div>
                        <details class="meaning-item" open="">
                          <summary>1</summary>
                          <ul>
                            <li>knife</li>
                          </ul>
                        </details>
                      </div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">勹</span>
                          </summary>
                          <div class="pinyin">bāo</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">RADICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/勹-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/勹-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div>
                              <details class="meaning-item" open="">
                                <summary>1</summary>
                                <ul>
                                  <li>wrap</li>
                                </ul>
                              </details>
                            </div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div>
                              <details class="components-item">
                                <summary>
                                  <span class="hanzi">㇒</span>
                                </summary>
                                <div class="pinyin">㇒</div>
                                <span class="hanzi-type-block"
                                  >Type:
                                  <span class="hanzi-type">GRAPHICAL</span>
                                </span>
                                <span class="sound"
                                  ><audio
                                    controls=""
                                    src="assets/㇒-sound.mp3"
                                  ></audio
                                ></span>
                                <details class="strokes" open>
                                  <summary>Strokes:</summary>
                                  <div>
                                    <img
                                      class="animated-gif"
                                      src="assets/㇒-strokes.gif"
                                    />
                                  </div>
                                </details>
                                <details class="meaning" open>
                                  <summary>Meaning:</summary>
                                  <div></div>
                                </details>
                                <details class="notes" open>
                                  <summary>Notes:</summary>
                                </details>
                                <details class="components" open>
                                  <summary>Components:</summary>
                                  <div></div>
                                </details>
                              </details>
                              <details class="components-item">
                                <summary>
                                  <span class="hanzi">㇆</span>
                                </summary>
                                <div class="pinyin">㇆</div>
                                <span class="hanzi-type-block"
                                  >Type:
                                  <span class="hanzi-type">GRAPHICAL</span>
                                </span>
                                <span class="sound"
                                  ><audio
                                    controls=""
                                    src="assets/㇆-sound.mp3"
                                  ></audio
                                ></span>
                                <details class="strokes" open>
                                  <summary>Strokes:</summary>
                                  <div>
                                    <img
                                      class="animated-gif"
                                      src="assets/㇆-strokes.gif"
                                    />
                                  </div>
                                </details>
                                <details class="meaning" open>
                                  <summary>Meaning:</summary>
                                  <div></div>
                                </details>
                                <details class="notes" open>
                                  <summary>Notes:</summary>
                                </details>
                                <details class="components" open>
                                  <summary>Components:</summary>
                                  <div></div>
                                </details>
                              </details>
                            </div>
                          </details>
                        </details>
                      </div>
                    </details>
                  </details>
                </div>
              </details>
            </details>
          </div>
        </details>
      </details>
      <details class="components-item">
        <summary>
          <span class="hanzi">好</span>
        </summary>
        <div class="pinyin">[ hǎo | hào ]</div>
        <span class="hanzi-type-block"
          >Type:
          <span class="hanzi-type">WORD</span>
        </span>
        <span class="sound"
          ><audio controls="" src="assets/好-sound.mp3"></audio
        ></span>
        <details class="strokes" open>
          <summary>Strokes:</summary>
          <div>
            <img class="animated-gif" src="assets/好-strokes.gif" />
          </div>
        </details>
        <details class="meaning" open>
          <summary>Meaning:</summary>
          <div>
            <details class="meaning-item" open="">
              <summary>hǎo</summary>
              <ul>
                <li>good</li>
                <li>well</li>
                <li>proper</li>
                <li>good to</li>
                <li>easy to</li>
                <li>very</li>
                <li>so</li>
                <li>(suffix indicating completion or readiness)</li>
                <li>(of two people) close</li>
                <li>on intimate terms</li>
                <li>(after a personal pronoun) hello</li>
              </ul>
            </details>
            <details class="meaning-item" open="">
              <summary>hào</summary>
              <ul>
                <li>to be fond of</li>
                <li>to have a tendency to</li>
                <li>to be prone to</li>
              </ul>
            </details>
          </div>
        </details>
        <details class="notes" open>
          <summary>Notes:</summary>
        </details>
        <details class="components" open>
          <summary>Components:</summary>
          <div>
            <details class="components-item">
              <summary>
                <span class="hanzi">女</span>
              </summary>
              <div class="pinyin">[ nǚ | nǜ | rǔ ]</div>
              <span class="hanzi-type-block"
                >Type:
                <span class="hanzi-type">RADICAL</span>
              </span>
              <span class="sound"
                ><audio controls="" src="assets/女-sound.mp3"></audio
              ></span>
              <details class="strokes" open>
                <summary>Strokes:</summary>
                <div>
                  <img class="animated-gif" src="assets/女-strokes.gif" />
                </div>
              </details>
              <details class="meaning" open>
                <summary>Meaning:</summary>
                <div>
                  <details class="meaning-item" open="">
                    <summary>1</summary>
                    <ul>
                      <li>woman</li>
                    </ul>
                  </details>
                </div>
              </details>
              <details class="notes" open>
                <summary>Notes:</summary>
              </details>
              <details class="components" open>
                <summary>Components:</summary>
                <div>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">㇛</span>
                    </summary>
                    <div class="pinyin">㇛</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">GRAPHICAL</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/㇛-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/㇛-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div></div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div></div>
                    </details>
                  </details>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">丆</span>
                    </summary>
                    <div class="pinyin">hǎn</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">WORD</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/丆-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/丆-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div>
                        <details class="meaning-item" open="">
                          <summary>xx</summary>
                          <ul>
                            <li>
                              one of the characters used in kwukyel (phonetic
                              &quot;myeon&quot;), an ancient Korean writing
                              system
                            </li>
                          </ul>
                        </details>
                      </div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">一</span>
                          </summary>
                          <div class="pinyin">[ yī | yí | yì ]</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">RADICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/一-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/一-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div>
                              <details class="meaning-item" open="">
                                <summary>1</summary>
                                <ul>
                                  <li>one</li>
                                </ul>
                              </details>
                            </div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div></div>
                          </details>
                        </details>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">丿</span>
                          </summary>
                          <div class="pinyin">[ piě | yì ]</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">RADICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/丿-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/丿-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div>
                              <details class="meaning-item" open="">
                                <summary>1</summary>
                                <ul>
                                  <li>bend</li>
                                </ul>
                              </details>
                            </div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div></div>
                          </details>
                        </details>
                      </div>
                    </details>
                  </details>
                </div>
              </details>
            </details>
            <details class="components-item">
              <summary>
                <span class="hanzi">子</span>
              </summary>
              <div class="pinyin">[ zi | zǐ ]</div>
              <span class="hanzi-type-block"
                >Type:
                <span class="hanzi-type">RADICAL</span>
              </span>
              <span class="sound"
                ><audio controls="" src="assets/子-sound.mp3"></audio
              ></span>
              <details class="strokes" open>
                <summary>Strokes:</summary>
                <div>
                  <img class="animated-gif" src="assets/子-strokes.gif" />
                </div>
              </details>
              <details class="meaning" open>
                <summary>Meaning:</summary>
                <div>
                  <details class="meaning-item" open="">
                    <summary>1</summary>
                    <ul>
                      <li>child</li>
                    </ul>
                  </details>
                </div>
              </details>
              <details class="notes" open>
                <summary>Notes:</summary>
              </details>
              <details class="components" open>
                <summary>Components:</summary>
                <div>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">一</span>
                    </summary>
                    <div class="pinyin">[ yī | yí | yì ]</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">RADICAL</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/一-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/一-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div>
                        <details class="meaning-item" open="">
                          <summary>1</summary>
                          <ul>
                            <li>one</li>
                          </ul>
                        </details>
                      </div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div></div>
                    </details>
                  </details>
                  <details class="components-item">
                    <summary>
                      <span class="hanzi">了</span>
                    </summary>
                    <div class="pinyin">[ le | liǎo | liào ]</div>
                    <span class="hanzi-type-block"
                      >Type:
                      <span class="hanzi-type">WORD</span>
                    </span>
                    <span class="sound"
                      ><audio controls="" src="assets/了-sound.mp3"></audio
                    ></span>
                    <details class="strokes" open>
                      <summary>Strokes:</summary>
                      <div>
                        <img class="animated-gif" src="assets/了-strokes.gif" />
                      </div>
                    </details>
                    <details class="meaning" open>
                      <summary>Meaning:</summary>
                      <div>
                        <details class="meaning-item" open="">
                          <summary>le</summary>
                          <ul>
                            <li>(completed action marker)</li>
                            <li>
                              (modal particle indicating change of state,
                              situation now)
                            </li>
                            <li>
                              (modal particle intensifying preceding clause)
                            </li>
                          </ul>
                        </details>
                        <details class="meaning-item" open="">
                          <summary>liǎo</summary>
                          <ul>
                            <li>to finish</li>
                            <li>to achieve</li>
                            <li>variant of 瞭|了[liao3]</li>
                            <li>to understand clearly</li>
                          </ul>
                        </details>
                        <details class="meaning-item" open="">
                          <summary>liǎo</summary>
                          <ul>
                            <li>(of eyes) bright</li>
                            <li>clear-sighted</li>
                            <li>to understand clearly</li>
                          </ul>
                        </details>
                        <details class="meaning-item" open="">
                          <summary>liào</summary>
                          <ul>
                            <li>unofficial variant of 瞭[liao4]</li>
                          </ul>
                        </details>
                      </div>
                    </details>
                    <details class="notes" open>
                      <summary>Notes:</summary>
                    </details>
                    <details class="components" open>
                      <summary>Components:</summary>
                      <div>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">亅</span>
                          </summary>
                          <div class="pinyin">jué</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">RADICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/亅-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/亅-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div>
                              <details class="meaning-item" open="">
                                <summary>1</summary>
                                <ul>
                                  <li>hook</li>
                                </ul>
                              </details>
                            </div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div></div>
                          </details>
                        </details>
                        <details class="components-item">
                          <summary>
                            <span class="hanzi">㇇</span>
                          </summary>
                          <div class="pinyin">㇇</div>
                          <span class="hanzi-type-block"
                            >Type:
                            <span class="hanzi-type">GRAPHICAL</span>
                          </span>
                          <span class="sound"
                            ><audio
                              controls=""
                              src="assets/㇇-sound.mp3"
                            ></audio
                          ></span>
                          <details class="strokes" open>
                            <summary>Strokes:</summary>
                            <div>
                              <img
                                class="animated-gif"
                                src="assets/㇇-strokes.gif"
                              />
                            </div>
                          </details>
                          <details class="meaning" open>
                            <summary>Meaning:</summary>
                            <div></div>
                          </details>
                          <details class="notes" open>
                            <summary>Notes:</summary>
                          </details>
                          <details class="components" open>
                            <summary>Components:</summary>
                            <div></div>
                          </details>
                        </details>
                      </div>
                    </details>
                  </details>
                </div>
              </details>
            </details>
          </div>
        </details>
      </details>
    </div>
  </details>
</details>

## Тексты и диалоги

Все уроки содержат как минимум один диалог и один текст.
Мне не нравится читать и учить диалоги в pdf по нескольким причинам.

- Постоянно смотреть произношение и перевод новых слов (или уже знакомых) занимает очень много времени и сил.

- Когда под каждым словом есть пиньинь, очень легко посмотреть произношение и сразу его забыть.

Хотелось бы просто навести курсор на новое слово в тексте и посмотреть его произношение и перевод.

Пример из [диалога 15 урока](lessons/lesson_15/dialogue1.md):

8. <b><u>迪玛</u></b>：除了<abbr title='zhìzuò - вырабатывать; производить'>制作</abbr><abbr title='biāoběn - образец, модель, экспонат / препарат'>标本</abbr>，我还不太会用<abbr title='xiǎnwēijìng - микроскоп'>显微镜</abbr>。我不知道怎么<abbr title='tiáojié - регулировать, настраивать'>调节</abbr><abbr title='shìyě - обзор, поле зрения'>视野</abbr>中的<abbr title='liàngdù - физ. яркость; блеск, освещение'>亮度</abbr>。

# Anki

[Anki](https://apps.ankiweb.net/) is a great tool for memorizing words.

## Get started

- Download the anki_deck.apkg file in the root of this repo, by cloning the repo f.e.
- Install Anki.
- Import anki_deck.apkg to Anki.
  Top left corner → File → Import → Select anki_deck.apkg

## Learn new words

https://github.com/user-attachments/assets/3f6c0a30-70eb-4616-a798-df0706ac4cf5

## Contribute

Not supported yet 😅

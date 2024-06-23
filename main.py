import keyboard

def on_key_event(event):
    if event.name == 'q':
        print("Wykryto klawisz: 'q'. Program zakonczy dzialanie.")
        return True
    elif event.name == 'a':
        print("Wykryto klawisz: 'a'. Akcja A wykonana.")
    elif event.name == 'b':
        print("Wykryto klawisz: 'b'. Akcja B wykonana.")
    elif event.name == 'ctrl+alt+del':
        print("Wykryto sekwencje klawiszy: 'ctrl+alt+del'. Akcja C wykonana.")
    return False

def main():
    print("Nacisnij 'q', aby zakonczyc program.")
    print("Nacisnij 'a', aby wykonac Akcje A.")
    print("Nacisnij 'b', aby wykonac Akcje B.")
    print("Nacisnij 'ctrl+alt+del', aby wykonac Akcje C.")
    print("Oczekiwanie na zdarzenia klawiatury...")

    keyboard.on_press(on_key_event)
    keyboard.wait('q')

if __name__ == "__main__":
    main()